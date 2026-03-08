import asyncio
import signal
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import ACCESS_MODE, API_TOKEN
from handlers import content_router, errors_router, helpers_router, menu_router
from loguru import logger
from middleware import AccessMiddleware

# ✅ Создаём папку для логов
Path("logs").mkdir(exist_ok=True)

# ✅ Настройка loguru
logger.remove()

# Консоль
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> | <level>{message}</level>",
    level="INFO",
    colorize=True,
)

# Файл (все логи)
logger.add(
    "logs/bot_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="7 days",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name} | {message}",
    encoding="utf-8",
)

# Файл (только ошибки)
logger.add(
    "logs/errors_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="7 days",
    level="ERROR",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name} | {message} | {exception}",
    encoding="utf-8",
)

logger.info("🚀 Инициализация бота...")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# ✅ Graceful shutdown
async def shutdown():
    """Корректное завершение работы"""
    logger.info("🛑 Завершение работы бота...")
    await bot.session.close()
    await dp.storage.close()
    logger.info("✅ Все соединения закрыты")


def signal_handler(signum, frame):
    logger.info(f"📴 Получен сигнал {signum}")
    asyncio.create_task(shutdown())
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Middleware
if ACCESS_MODE is not None:
    dp.message.middleware(AccessMiddleware())

# Роутеры
dp.include_router(errors_router)
dp.include_router(content_router)
dp.include_router(menu_router)
dp.include_router(helpers_router)


async def main():
    try:
        logger.info("🚀 Запуск polling...")
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("🛑 Бот остановлен (KeyboardInterrupt)")
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}", exc_info=True)
        raise
    finally:
        await shutdown()


if __name__ == "__main__":
    asyncio.run(main())
