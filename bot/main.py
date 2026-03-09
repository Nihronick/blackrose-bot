import asyncio
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import ACCESS_MODE, API_TOKEN
from handlers import content_router, errors_router, menu_router
from loguru import logger
from middleware import AccessMiddleware

# Папка для логов
Path("logs").mkdir(exist_ok=True)

# Настройка loguru
logger.remove()

# Консоль
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level:<8}</level> | <cyan>{name}</cyan> | <level>{message}</level>",
    level="INFO",
    colorize=True,
)

# Файл (все логи)
logger.add(
    "logs/bot_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="7 days",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {name} | {message}",
    encoding="utf-8",
)

# Файл (только ошибки)
logger.add(
    "logs/errors_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="7 days",
    level="ERROR",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {name} | {message} | {exception}",
    encoding="utf-8",
)

# Проброс стандартного logging в loguru
import logging


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

logger.info("🚀 Инициализация бота...")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Middleware
if ACCESS_MODE and ACCESS_MODE != "off":
    dp.message.middleware(AccessMiddleware())
    dp.callback_query.middleware(AccessMiddleware())

# Роутеры
dp.include_router(errors_router)
dp.include_router(content_router)
dp.include_router(menu_router)


async def shutdown():
    """Корректное завершение работы"""
    logger.info("🛑 Завершение работы бота...")
    await bot.session.close()
    await dp.storage.close()
    logger.info("✅ Все соединения закрыты")


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