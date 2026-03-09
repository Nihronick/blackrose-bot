import asyncio
import logging

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext

from config import DELETE_DELAY

logger = logging.getLogger(__name__)


async def get_user_messages(state: FSMContext) -> list[int]:
    """Получить список ID сообщений с контентом"""
    data = await state.get_data()
    return data.get("content_messages", [])


async def get_menu_message_id(state: FSMContext) -> int | None:
    """Получить ID текущего сообщения меню"""
    data = await state.get_data()
    return data.get("menu_message_id")


async def add_user_message(message_id: int, state: FSMContext):
    """Добавить ID сообщения с контентом в список"""
    data = await state.get_data()
    messages = data.get("content_messages", [])
    messages.append(message_id)
    await state.update_data(content_messages=messages)


async def set_menu_message_id(message_id: int, state: FSMContext):
    """Сохранить ID сообщения меню"""
    await state.update_data(menu_message_id=message_id)


async def clear_user_messages(state: FSMContext, bot: Bot):
    """Удалить все сообщения с контентом (не меню!)"""
    data = await state.get_data()
    messages = data.get("content_messages", [])
    chat_id = data.get("chat_id")

    # Пробуем получить chat_id из state, если нет — пропускаем
    if not chat_id and not messages:
        return

    for msg_id in messages:
        try:
            # chat_id берём из сохранённого значения
            if chat_id:
                await bot.delete_message(chat_id=chat_id, message_id=msg_id)
                await asyncio.sleep(DELETE_DELAY)
        except Exception as e:
            logger.debug(f"Не удалось удалить сообщение {msg_id}: {e}")

    await state.update_data(content_messages=[])


async def send_content_messages(message, messages_data: list, state: FSMContext, bot: Bot):
    """
    Отправляет несколько сообщений с контентом.
    message — объект Message.
    """
    # Сохраняем chat_id для будущей очистки
    await state.update_data(chat_id=message.chat.id)

    await clear_user_messages(state, bot)

    for method_name, params in messages_data:
        try:
            method = getattr(message, method_name)
            msg = await method(**params)

            if isinstance(msg, list):
                for m in msg:
                    await add_user_message(m.message_id, state)
            else:
                await add_user_message(msg.message_id, state)

            await asyncio.sleep(DELETE_DELAY)
        except Exception as e:
            logger.error(f"Ошибка отправки {method_name}: {e}")