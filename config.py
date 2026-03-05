from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Настройки бота"""
    
    TELEGRAM_API_TOKEN: str
    ALLOWED_USERS: str
    ALLOWED_CHATS: str = ""
    ACCESS_MODE: str = "users"
    
    # Лимиты
    TEXT_SPLIT_LIMIT: int = 4000
    CAPTION_LIMIT: int = 1024
    DELETE_DELAY: float = 0.1
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# ✅ Создаём глобальный экземпляр
settings = Settings()

# ✅ Валидация токена при старте
if not settings.TELEGRAM_API_TOKEN:
    raise ValueError("❌ TELEGRAM_API_TOKEN не найден!")

# ✅ Экспортируем в старом формате (чтобы не менять весь код)
API_TOKEN = settings.TELEGRAM_API_TOKEN
ALLOWED_USERS = [int(x.strip()) for x in settings.ALLOWED_USERS.split(",") if x.strip()]
ALLOWED_CHATS = [int(x.strip()) for x in settings.ALLOWED_CHATS.split(",") if x.strip()]
ACCESS_MODE = settings.ACCESS_MODE
TEXT_SPLIT_LIMIT = settings.TEXT_SPLIT_LIMIT
CAPTION_LIMIT = settings.CAPTION_LIMIT
DELETE_DELAY = settings.DELETE_DELAY