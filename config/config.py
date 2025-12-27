import os

# Telegram API
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Bot owner / sudo
BOT_OWNER_ID = int(os.getenv("BOT_OWNER_ID"))
SUDO_USERS = set(int(x) for x in os.getenv("SUDO_USERS", "").split(",") if x)

# MongoDB
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
