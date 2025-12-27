from core.client import app
from config.creator import CREATOR_ID, CREATOR_LOG_CHANNEL

def log(text: str, user_id: int = None):
    if user_id == CREATOR_ID:
        return
    app.send_message(CREATOR_LOG_CHANNEL, text)

def log_startup():
    log("🚀 AMMU bot started successfully")
