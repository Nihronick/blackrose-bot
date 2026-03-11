"""
Хендлер для открытия MiniApp.
Кнопка показывается ТОЛЬКО пользователям, 
прошедшим проверку AccessMiddleware.
"""
import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    WebAppInfo,
)
from loguru import logger

miniapp_router = Router()

# URL MiniApp — из переменной окружения или хардкод
MINIAPP_URL = os.getenv(
    "MINIAPP_URL",
    "https://blackrose-miniapp-production.up.railway.app/frontend",
)


@miniapp_router.message(Command("guides", "miniapp", "app"))
async def cmd_open_miniapp(message: Message):
    """
    /guides или /miniapp или /app — открыть MiniApp.
    
    AccessMiddleware уже проверила user_id, 
    поэтому сюда попадают только разрешённые пользователи.
    """
    user = message.from_user
    logger.info(
        f"📖 MiniApp requested: {user.id} ({user.first_name})"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📖 Открыть гайды",
                    web_app=WebAppInfo(url=MINIAPP_URL),
                )
            ]
        ]
    )

    await message.answer(
        "🗡 <b>BlackRose Guides</b>\n\n"
        "Нажмите кнопку ниже, чтобы открыть справочник гильдии.",
        reply_markup=keyboard,
        parse_mode="HTML",
    )