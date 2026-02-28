# test_imports.py
from utils import (
    get_main_keyboard,
    get_submenu_keyboard,
    get_navigation_keyboard,
    split_text,
    get_user_messages,
    add_user_message,
    clear_user_messages,
    send_menu_message,
    send_content_messages
)
from middleware import AccessMiddleware
from handlers import menu_router, content_router, helpers_router

print("✅ Все импорты работают!")