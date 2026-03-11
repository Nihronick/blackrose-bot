'''import logging

from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaPhoto, Message
from config import CAPTION_LIMIT
from data.guides import CONTENT, SUBMENUS
from utils import get_content_keyboard, get_main_keyboard, get_submenu_keyboard, send_content_messages, split_text

logger = logging.getLogger(__name__)

router = Router()

# Список всех кнопок подменю
ALL_SUBMENU_ITEMS = [item[1] for items in SUBMENUS.values() for item in items]


@router.message(F.text == "🔙 Назад к списку")
async def back_to_submenu(message: Message, state: FSMContext, bot: Bot):
    """Возврат в подменю"""
    logger.info("🔙 Возврат в подменю")

    data = await state.get_data()
    current_category = data.get("current_category")

    if not current_category or current_category not in SUBMENUS:
        await message.answer("📂 Выберите раздел:", reply_markup=get_main_keyboard())
        return

    await message.answer(
        "📂 Выберите материал:",
        reply_markup=get_submenu_keyboard(current_category),
    )


# Кнопки ПОДМЕНЮ
@router.message(F.text.in_(ALL_SUBMENU_ITEMS))
async def process_submenu_text(message: Message, state: FSMContext, bot: Bot):
    """Обработка кнопок подменю (выбор материала)"""
    item_text = message.text
    logger.info(f"📦 Получен текст подменю: {item_text}")

    data = await state.get_data()
    category_key = data.get("current_category")

    # Если категории нет — ищем по всем
    if not category_key:
        category_key = _find_category_by_item(item_text)
        if category_key:
            await state.update_data(current_category=category_key)

    if not category_key:
        logger.warning(f"❌ Не найдена категория для: {item_text}")
        return

    # Находим item_key
    item_key = _find_item_key(category_key, item_text)
    if not item_key:
        logger.warning(f"❌ Не найден item_key для: {item_text}")
        return

    logger.info(f"📦 Загрузка контента: {item_key} (категория: {category_key})")

    content = CONTENT.get(item_key)
    if not content:
        await message.answer("❌ Информация не найдена.")
        return

    text = content.get("text", "")
    photo = content.get("photo")
    video = content.get("video")
    document = content.get("document")
    keyboard = get_content_keyboard(category_key)

    try:
        messages_data = _build_messages(text, photo, video, document, keyboard)
        await send_content_messages(message, messages_data, state, bot)
    except TelegramBadRequest as e:
        logger.error(f"❌ Ошибка отправки контента: {e}")
        if text:
            await message.answer(
                f"⚠️ Не удалось загрузить медиа:\n\n{text}",
                reply_markup=keyboard,
                parse_mode="HTML",
            )


def _find_category_by_item(item_text: str) -> str | None:
    """Найти категорию по тексту кнопки подменю"""
    for cat_key, items in SUBMENUS.items():
        for _callback, text in items:
            if text == item_text:
                return cat_key
    return None


def _find_item_key(category_key: str, item_text: str) -> str | None:
    """Найти ключ элемента в категории"""
    for callback, text in SUBMENUS[category_key]:
        if text == item_text:
            return callback
    return None


def _build_messages(text: str, photo, video, document, keyboard) -> list:
    """Собрать список сообщений для отправки"""
    messages_data = []

    # Только текст
    if not photo and not video and not document:
        return _build_text_only(text, keyboard)

    # Видео
    if video:
        return _build_video(text, video, keyboard)

    # Документы
    if document:
        return _build_document(text, document, keyboard)

    # Фото
    if photo:
        return _build_photo(text, photo, keyboard)

    return messages_data


def _build_text_only(text: str, keyboard) -> list:
    """Сообщения с текстом без медиа"""
    parts = split_text(text) if text else ["❌ Нет контента"]
    messages_data = []
    for i, part in enumerate(parts):
        header = f"📄 Часть {i + 1}/{len(parts)}\n\n" if len(parts) > 1 else ""
        markup = keyboard if i == len(parts) - 1 else None
        messages_data.append(("answer", {"text": header + part, "reply_markup": markup, "parse_mode": "HTML"}))
    return messages_data


def _build_video(text: str, video, keyboard) -> list:
    """Сообщения с видео"""
    messages_data = []
    caption = text[:CAPTION_LIMIT] if text and len(text) > CAPTION_LIMIT else text
    video_list = video if isinstance(video, list) else [video]

    for i, vid in enumerate(video_list):
        cap = caption if i == 0 else ""
        markup = keyboard if i == len(video_list) - 1 else None
        messages_data.append(("answer_video", {"video": vid, "caption": cap, "reply_markup": markup}))

    if text and len(text) > CAPTION_LIMIT:
        messages_data.append(("answer", {"text": text[CAPTION_LIMIT:], "reply_markup": keyboard, "parse_mode": "HTML"}))

    return messages_data


def _build_document(text: str, document, keyboard) -> list:
    """Сообщения с документами"""
    messages_data = []

    if text:
        text_parts = split_text(text)
        for i, part in enumerate(text_parts):
            markup = keyboard if i == len(text_parts) - 1 else None
            messages_data.append(("answer", {"text": part, "reply_markup": markup, "parse_mode": "HTML"}))

    doc_list = document if isinstance(document, list) else [document]
    for i, doc in enumerate(doc_list):
        short_caption = f"📎 Файл {i + 1}/{len(doc_list)}" if len(doc_list) > 1 else ""
        markup = keyboard if i == len(doc_list) - 1 else None
        messages_data.append(
            ("answer_document", {"document": doc, "caption": short_caption if i == 0 else "", "reply_markup": markup})
        )

    return messages_data


def _build_photo(text: str, photo, keyboard) -> list:
    """Сообщения с фото"""
    messages_data = []
    caption = text[:CAPTION_LIMIT] if text and len(text) > CAPTION_LIMIT else text

    if isinstance(photo, list) and len(photo) > 1:
        media_group = [InputMediaPhoto(media=photo[0], caption=caption)]
        for img in photo[1:]:
            media_group.append(InputMediaPhoto(media=img))
        messages_data.append(("answer_media_group", {"media": media_group}))

        if text and len(text) > CAPTION_LIMIT:
            messages_data.append(
                ("answer", {"text": text[CAPTION_LIMIT:], "reply_markup": keyboard, "parse_mode": "HTML"})
            )
        else:
            messages_data.append(("answer", {"text": "\u200e", "reply_markup": keyboard}))
    else:
        photo_id = photo[0] if isinstance(photo, list) else photo
        messages_data.append(("answer_photo", {"photo": photo_id, "caption": caption, "reply_markup": keyboard}))

        if text and len(text) > CAPTION_LIMIT:
            messages_data.append(
                ("answer", {"text": text[CAPTION_LIMIT:], "reply_markup": keyboard, "parse_mode": "HTML"})
            )

    return messages_data
'''