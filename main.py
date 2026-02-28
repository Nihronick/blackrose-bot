import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import API_TOKEN, ACCESS_MODE
from middleware import AccessMiddleware
from handlers import menu_router, content_router, helpers_router

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

if ACCESS_MODE is not None:
    dp.message.middleware(AccessMiddleware())

# ✅ content_router ПЕРВЫЙ (обрабатывает кнопки подменю)
dp.include_router(content_router)   # 1️⃣ Контент (более специфичный)
dp.include_router(menu_router)      # 2️⃣ Главное меню
dp.include_router(helpers_router)   # 3️⃣ File ID хелперы


async def main():
    logger.info("🚀 Запуск бота...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())