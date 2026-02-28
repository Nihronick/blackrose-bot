import logging
from aiogram import Bot, F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from utils import (
    split_text,
    send_content_messages,
    get_content_keyboard,
    get_submenu_keyboard,
    get_main_keyboard
)
from guides import CONTENT, SUBMENUS, MAIN_CATEGORIES
from config import CAPTION_LIMIT

logger = logging.getLogger(__name__)

router = Router()


# ✅ Список всех кнопок подменю
ALL_SUBMENU_ITEMS = [item[1] for items in SUBMENUS.values() for item in items]


@router.message(F.text == "🔙 Назад к списку")
async def back_to_submenu(message: Message, state: FSMContext, bot: Bot):
    """Возврат в подменю"""
    logger.info(f"🔙 Возврат в подменю")
    
    data = await state.get_data()
    current_category = data.get("current_category")
    
    if not current_category or current_category not in SUBMENUS:
        await message.answer(
            "📂 Выберите раздел:",
            reply_markup=get_main_keyboard()
        )
        return
    
    await message.answer(
        "📂 Выберите материал:",
        reply_markup=get_submenu_keyboard(current_category)
    )


@router.message(F.text == "🏠 Главное меню")
async def back_to_main_from_content(message: Message, state: FSMContext, bot: Bot):
    """Возврат в главное меню из контента"""
    logger.info(f"🏠 Возврат в главное меню из контента")
    await message.answer(
        "👋 Главное меню:",
        reply_markup=get_main_keyboard()
    )


# ✅ СТРОГИЙ ФИЛЬТР: только кнопки ПОДМЕНЮ
@router.message(F.text.in_(ALL_SUBMENU_ITEMS))
async def process_submenu_text(message: Message, state: FSMContext, bot: Bot):
    """Обработка кнопок подменю (выбор материала)"""
    item_text = message.text
    logger.info(f"📦 Получен текст подменю: {item_text}")
    
    # ✅ Получаем текущую категорию
    data = await state.get_data()
    category_key = data.get("current_category")
    
    # ✅ Если категории нет — ищем по всем категориям
    if not category_key:
        for cat_key, items in SUBMENUS.items():
            for callback, text in items:
                if text == item_text:
                    category_key = cat_key
                    await state.update_data(current_category=cat_key)
                    logger.info(f"   ✅ Найдена категория: {category_key}")
                    break
            if category_key:
                break
    
    if not category_key:
        logger.warning(f"❌ Не найдена категория для: {item_text}")
        return
    
    # ✅ Находим item_key
    item_key = None
    for callback, text in SUBMENUS[category_key]:
        if text == item_text:
            item_key = callback
            break
    
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
    
    messages_data = []
    
    # 📝 ТОЛЬКО ТЕКСТ
    if not photo and not video and not document:
        parts = split_text(text) if text else ["❌ Нет контента"]
        for i, part in enumerate(parts):
            header = f"📄 Часть {i + 1}/{len(parts)}\n\n" if len(parts) > 1 else ""
            markup = keyboard if i == len(parts) - 1 else None
            messages_data.append(("answer", {
                "text": header + part,
                "reply_markup": markup,
                "parse_mode": "HTML"
            }))
        
        await send_content_messages(message, messages_data, state, bot)
        return
    
    try:
        # 🎥 ВИДЕО
        if video:
            caption = text[:CAPTION_LIMIT] if text and len(text) > CAPTION_LIMIT else text
            video_list = video if isinstance(video, list) else [video]
            
            for i, vid in enumerate(video_list):
                cap = caption if i == 0 else ""
                markup = keyboard if i == len(video_list) - 1 else None
                messages_data.append(("answer_video", {
                    "video": vid,
                    "caption": cap,
                    "reply_markup": markup
                }))
            
            if text and len(text) > CAPTION_LIMIT:
                messages_data.append(("answer", {
                    "text": text[CAPTION_LIMIT:],
                    "reply_markup": keyboard,
                    "parse_mode": "HTML"
                }))
        
        # 📄 ДОКУМЕНТЫ
        elif document:
            if text:
                text_parts = split_text(text)
                for i, part in enumerate(text_parts):
                    markup = keyboard if i == len(text_parts) - 1 else None
                    messages_data.append(("answer", {
                        "text": part,
                        "reply_markup": markup,
                        "parse_mode": "HTML"
                    }))
            
            doc_list = document if isinstance(document, list) else [document]
            for i, doc in enumerate(doc_list):
                short_caption = f"📎 Файл {i+1}/{len(doc_list)}" if len(doc_list) > 1 else ""
                markup = keyboard if i == len(doc_list) - 1 else None
                messages_data.append(("answer_document", {
                    "document": doc,
                    "caption": short_caption if i == 0 else "",
                    "reply_markup": markup
                }))
        
        # 📸 ФОТО
        elif photo:
            caption = text[:CAPTION_LIMIT] if text and len(text) > CAPTION_LIMIT else text
            
            if isinstance(photo, list) and len(photo) > 1:
                from aiogram.types import InputMediaPhoto
                media_group = [InputMediaPhoto(media=photo[0], caption=caption)]
                for img in photo[1:]:
                    media_group.append(InputMediaPhoto(media=img))
                
                messages_data.append(("answer_media_group", {"media": media_group}))
                
                if text and len(text) > CAPTION_LIMIT:
                    messages_data.append(("answer", {
                        "text": text[CAPTION_LIMIT:],
                        "reply_markup": keyboard,
                        "parse_mode": "HTML"
                    }))
                else:
                    messages_data.append(("answer", {
                        "text": "\u200e",
                        "reply_markup": keyboard
                    }))
            else:
                photo_id = photo[0] if isinstance(photo, list) else photo
                messages_data.append(("answer_photo", {
                    "photo": photo_id,
                    "caption": caption,
                    "reply_markup": keyboard
                }))
                
                if text and len(text) > CAPTION_LIMIT:
                    messages_data.append(("answer", {
                        "text": text[CAPTION_LIMIT:],
                        "reply_markup": keyboard,
                        "parse_mode": "HTML"
                    }))
        
        await send_content_messages(message, messages_data, state, bot)
                    
    except TelegramBadRequest as e:
        logger.error(f"❌ Ошибка отправки контента: {e}")
        if text:
            await message.answer(
                f"⚠️ Не удалось загрузить медиа:\n\n{text}",
                reply_markup=keyboard,
                parse_mode="HTML"
            )