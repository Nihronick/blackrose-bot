import asyncio
import logging

from aiogram import Bot, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from config import DELETE_DELAY

logger = logging.getLogger(__name__)


async def get_user_messages(user_id: int, state: FSMContext) -> list[int]:
    """Получить список ID сообщений с контентом"""
    data = await state.get_data()
    return data.get(f"content_messages_{user_id}", [])


async def get_menu_message_id(user_id: int, state: FSMContext) -> int | None:
    """Получить ID текущего сообщения меню"""
    data = await state.get_data()
    return data.get(f"menu_message_{user_id}")


async def add_user_message(user_id: int, message_id: int, state: FSMContext):
    """Добавить ID сообщения с контентом в список"""
    data = await state.get_data()
    messages = data.get(f"content_messages_{user_id}", [])
    messages.append(message_id)
    await state.update_data(**{f"content_messages_{user_id}": messages})


async def set_menu_message_id(user_id: int, message_id: int, state: FSMContext):
    """Сохранить ID сообщения меню"""
    await state.update_data(**{f"menu_message_{user_id}": message_id})


async def clear_user_messages(user_id: int, state: FSMContext, bot: Bot):
    """Удалить все сообщения с контентом (не меню!)"""
    messages = await get_user_messages(user_id, state)

    for msg_id in messages:
        try:
            await bot.delete_message(chat_id=user_id, message_id=msg_id)
            await asyncio.sleep(DELETE_DELAY)
        except Exception as e:
            logger.debug(f"Не удалось удалить сообщение {msg_id}: {e}")

    await state.update_data(**{f"content_messages_{user_id}": []})


async def _try_edit_menu(bot: Bot, user_id: int, menu_msg_id: int, text: str, reply_markup) -> bool:
    """
    Пытается отредактировать меню.
    Возвращает True при успехе, False при неудаче.
    """
    try:
        await bot.edit_message_text(
            text=text, chat_id=user_id, message_id=menu_msg_id, reply_markup=reply_markup, parse_mode="HTML"
        )
        return True
    except TelegramBadRequest as e:
        error = str(e)

        # ✅ Текст и клавиатура те же — это успех
        if "message is not modified" in error:
            return True

        # ✅ Сообщение удалено или содержит медиа — нельзя редактировать
        if "message to edit not found" in error or "there is no text" in error or "message can't be edited" in error:
            try:
                await bot.delete_message(chat_id=user_id, message_id=menu_msg_id)
            except Exception as e:
                logger.debug(f"Не удалось удалить: {e}")
            return False

        # ❌ Другая ошибка
        logger.error(f"❌ Ошибка редактирования меню {menu_msg_id}: {e}")
        return False


async def send_menu_message(callback: types.CallbackQuery, text: str, reply_markup, state: FSMContext, bot: Bot):
    """
    Отправляет сообщение меню.
    """
    user_id = callback.from_user.id
    callback_msg_id = callback.message.message_id

    menu_msg_id = await get_menu_message_id(user_id, state)

    logger.info(f"📋 send_menu_message: menu_msg_id={menu_msg_id}, callback_msg_id={callback_msg_id}")

    # ✅ Если есть tracked меню — пробуем редактировать
    if menu_msg_id:
        if await _try_edit_menu(bot, user_id, menu_msg_id, text, reply_markup):
            logger.info(f"✏️ Меню отредактировано (msg_id={menu_msg_id})")

            # ✅ Удаляем callback.message, если это не меню (контент)
            if callback_msg_id != menu_msg_id:
                try:
                    await callback.message.delete()
                    logger.info(f"🗑️ Удалено сообщение контента (msg_id={callback_msg_id})")
                except Exception as e:
                    logger.debug(f"Не удалось удалить: {e}")
            return

    # ✅ Очищаем контент
    await clear_user_messages(user_id, state, bot)

    # ✅ Удаляем callback.message, если оно ещё существует
    try:
        await callback.message.delete()
    except Exception as e:
        logger.debug(f"Не удалось удалить: {e}")

    # ✅ Отправляем НОВОЕ меню
    msg = await bot.send_message(chat_id=user_id, text=text, reply_markup=reply_markup, parse_mode="HTML")
    await set_menu_message_id(user_id, msg.message_id, state)
    logger.info(f"📤 Новое меню отправлено (msg_id={msg.message_id})")


async def send_content_messages(callback, messages_data: list, state: FSMContext, bot: Bot):
    """
    Отправляет несколько сообщений с контентом.
    callback может быть Message или CallbackQuery.
    """
    user_id = callback.from_user.id
    await clear_user_messages(user_id, state, bot)

    for method_name, params in messages_data:
        try:
            method = getattr(callback, method_name)
            msg = await method(**params)

            if isinstance(msg, list):
                for m in msg:
                    await add_user_message(user_id, m.message_id, state)
            else:
                await add_user_message(user_id, msg.message_id, state)

            await asyncio.sleep(DELETE_DELAY)
        except Exception as e:
            logger.error(f"Ошибка отправки {method_name}: {e}")
