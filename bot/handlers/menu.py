import logging

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from data.guides import MAIN_CATEGORIES, SUBMENUS
from utils import clear_user_messages, get_main_keyboard, get_submenu_keyboard, set_menu_message_id

logger = logging.getLogger(__name__)

router = Router()


@router.message(Command("start"))
@router.message(Command("menu"))
async def cmd_start(message: Message, state: FSMContext, bot: Bot):
    """Команда /start или /menu — показываем главное меню"""
    await show_main_menu(message, state, bot)


async def show_main_menu(message: Message, state: FSMContext, bot: Bot):
    """Показать главное меню"""
    await clear_user_messages(state, bot)
    await state.clear()

    msg = await message.answer(
        "👋 Привет! Выберите раздел справочника:",
        reply_markup=get_main_keyboard(),
    )
    await set_menu_message_id(msg.message_id, state)
    logger.info(f"📋 Меню создано (msg_id={msg.message_id})")


@router.message(F.text == "❌ Закрыть меню")
async def close_menu(message: Message, state: FSMContext):
    """Закрыть меню"""
    await state.clear()
    await message.answer(
        "Меню закрыто. Напишите /start чтобы открыть.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(F.text == "🏠 Главное меню")
async def back_to_main_menu(message: Message, state: FSMContext, bot: Bot):
    """Возврат в главное меню"""
    logger.info("🏠 Возврат в главное меню")
    await show_main_menu(message, state, bot)


@router.message(F.text == "🔙 В главное меню")
async def back_to_main_from_submenu(message: Message, state: FSMContext, bot: Bot):
    """Возврат в главное меню из подменю"""
    logger.info("🔙 Возврат в главное меню из подменю")
    await show_main_menu(message, state, bot)


# Кнопки ГЛАВНОГО меню
@router.message(F.text.in_(list(MAIN_CATEGORIES.values())))
async def process_category_text(message: Message, state: FSMContext, bot: Bot):
    """Обработка кнопок ГЛАВНОГО меню"""
    category_text = message.text
    logger.info(f"🔘 Получен текст: {category_text}")

    category_key = None
    for key, value in MAIN_CATEGORIES.items():
        if value == category_text:
            category_key = key
            logger.info(f"  ✅ Найдена категория: {category_key}")
            break

    if not category_key:
        return

    if category_key not in SUBMENUS:
        await message.answer("❌ Категория не найдена.")
        return

    await state.update_data(current_category=category_key)
    await message.answer(
        "📂 Выберите материал:",
        reply_markup=get_submenu_keyboard(category_key),
    )


# Обработка неизвестных сообщений — ПОСЛЕДНИЙ хендлер
@router.message()
async def handle_unknown_message(message: Message, state: FSMContext, bot: Bot):
    """Авто-меню при любом неизвестном сообщении"""
    data = await state.get_data()
    has_menu = data.get("menu_message_id")

    if not has_menu:
        logger.info("📋 Первое сообщение — показываем меню")
        await show_main_menu(message, state, bot)
