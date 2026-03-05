import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger

from config import ACCESS_MODE, API_TOKEN
from handlers import content_router, errors_router, helpers_router, menu_router
from middleware import AccessMiddleware

# ✅ Настройка loguru
logger.remove()  # Убираем стандартный handler
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> | <level>{message}</level>",
    level="INFO",
    colorize=True,
)

# ✅ Логирование в файл (опционально, для отладки)
logger.add(
    "logs/bot_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="7 days",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name} | {message}",
)

logger.info("🚀 Запуск бота...")

# ✅ Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# ✅ Middleware
if ACCESS_MODE is not None:
    dp.message.middleware(AccessMiddleware())

# ✅ Роутеры (ВАЖНО: errors_router первым!)
dp.include_router(errors_router)  # ⭐ Обработка ошибок
dp.include_router(content_router)  # 1️⃣ Контент (более специфичный)
dp.include_router(menu_router)  # 2️⃣ Главное меню
dp.include_router(helpers_router)  # 3️⃣ File ID хелперы


async def main():
    try:
        logger.info("🚀 Запуск polling...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}", exc_info=True)
        raise
    finally:
        await bot.session.close()
        logger.info("🛑 Бот остановлен")


if __name__ == "__main__":
    asyncio.run(main())
