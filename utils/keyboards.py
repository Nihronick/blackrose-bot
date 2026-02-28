from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

from guides import MAIN_CATEGORIES, SUBMENUS


def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню (Reply Keyboard)"""
    builder = ReplyKeyboardBuilder()
    
    for callback, text in MAIN_CATEGORIES.items():
        builder.button(text=text)
    
    builder.adjust(2)
    builder.button(text="❌ Закрыть меню")
    
    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False
    )


def get_submenu_keyboard(category_key: str) -> ReplyKeyboardMarkup:
    """
    Подменю категории (Reply Keyboard).
    """
    builder = ReplyKeyboardBuilder()
    items = SUBMENUS.get(category_key, [])
    
    for callback, text in items:
        builder.button(text=text)
    
    builder.adjust(3, repeat=True)
    builder.button(text="🔙 В главное меню")
    
    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False
    )


def get_content_keyboard(category_key: str | None = None) -> ReplyKeyboardMarkup:
    """
    Клавиатура навигации для контента.
    """
    builder = ReplyKeyboardBuilder()
    
    if category_key:
        builder.button(text="🔙 Назад к списку")
    
    builder.button(text="🏠 Главное меню")
    
    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False
    )


def get_close_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура с кнопкой открытия меню"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="📋 Открыть меню")
    return builder.as_markup(resize_keyboard=True)