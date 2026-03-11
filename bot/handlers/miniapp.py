"""
MiniApp handler — единственная основная функция бота.
Показывает кнопку WebApp при /start, /guides, /app
и как постоянную reply-клавиатуру.
"""
import os

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    WebAppInfo,
)
from loguru import logger

miniapp_router = Router()

MINIAPP_URL = os.getenv(
    "MINIAPP_URL",
    "https://blackrose-miniapp-production.up.railway.app/frontend",
)


def get_miniapp_reply_keyboard() -> ReplyKeyboardMarkup:
    """
    Reply-клавиатура с одной кнопкой WebApp.
    Всегда видна внизу — пользователю не нужно ничего искать.
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="📖 Открыть гайды",
                    web_app=WebAppInfo(url=MINIAPP_URL),
                )
            ]
        ],
        resize_keyboard=True,
        is_persistent=True,  # Клавиатура не скрывается
    )


def get_miniapp_inline_keyboard() -> InlineKeyboardMarkup:
    """Inline-кнопка WebApp (в сообщении)."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📖 Открыть гайды",
                    web_app=WebAppInfo(url=MINIAPP_URL),
                )
            ]
        ]
    )


@miniapp_router.message(CommandStart())
async def cmd_start(message: Message):
    """
    /start — приветствие + reply-клавиатура с кнопкой MiniApp.
    """
    user = message.from_user
    logger.info(f"👋 /start от {user.id} ({user.first_name})")

    await message.answer(
        f"👋 Привет, <b>{user.first_name}</b>!\n\n"
        f"🗡 Добро пожаловать в <b>BlackRose</b>.\n\n"
        f"Нажмите кнопку <b>«📖 Открыть гайды»</b> внизу экрана, "
        f"чтобы открыть справочник гильдии.",
        parse_mode="HTML",
        reply_markup=get_miniapp_reply_keyboard(),
    )


@miniapp_router.message(Command("guides", "miniapp", "app"))
async def cmd_guides(message: Message):
    """
    /guides — отправляет inline-кнопку + 
    убеждается что reply-клавиатура на месте.
    """
    user = message.from_user
    logger.info(f"📖 /guides от {user.id} ({user.first_name})")

    # Inline-кнопка в сообщении (можно нажать сразу)
    await message.answer(
        "🗡 <b>BlackRose Guides</b>\n\n"
        "Нажмите кнопку ниже или используйте кнопку внизу экрана.",
        parse_mode="HTML",
        reply_markup=get_miniapp_inline_keyboard(),
    )


@miniapp_router.message(Command("help"))
async def cmd_help(message: Message):
    """/help — справка."""
    logger.info(f"❓ /help от {message.from_user.id}")

    await message.answer(
        "📚 <b>Доступные команды:</b>\n\n"
        "/start — Показать приветствие и кнопку\n"
        "/guides — Открыть справочник гильдии\n"
        "/help — Эта справка\n\n"
        "💡 Кнопка <b>«📖 Открыть гайды»</b> всегда доступна "
        "внизу экрана.",
        parse_mode="HTML",
        reply_markup=get_miniapp_reply_keyboard(),
    )