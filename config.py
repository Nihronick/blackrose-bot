import os
from dotenv import load_dotenv

# ✅ Загружаем .env только локально (на Railway его нет)
if os.path.exists(".env"):
    load_dotenv()

# 🔑 API Token
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

if not API_TOKEN:
    raise ValueError("❌ TELEGRAM_API_TOKEN не найден!")

# 🔒 Доступ
ALLOWED_USERS_RAW = os.getenv("ALLOWED_USERS", "")
ALLOWED_USERS = [int(x.strip()) for x in ALLOWED_USERS_RAW.split(",") if x.strip()]

ACCESS_MODE = os.getenv("ACCESS_MODE", "users")

# 📝 Лимиты
TEXT_SPLIT_LIMIT = int(os.getenv("TEXT_SPLIT_LIMIT", 4000))
CAPTION_LIMIT = int(os.getenv("CAPTION_LIMIT", 1024))
DELETE_DELAY = float(os.getenv("DELETE_DELAY", 0.1))