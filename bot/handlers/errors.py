from aiogram import Router
from aiogram.types import ErrorEvent
from loguru import logger

router = Router()


@router.errors()
async def error_handler(event: ErrorEvent) -> bool:
    """
    Глобальный обработчик ошибок.
    """
    logger.error(f"❌ Ошибка в update {event.update.update_id}", exception=event.exception, exc_info=True)

    # ✅ Можно отправить уведомление админу
    # from aiogram import Bot
    # await bot.send_message(ADMIN_ID, f"❌ Ошибка: {event.exception}")

    return True  # Ошибка обработана
