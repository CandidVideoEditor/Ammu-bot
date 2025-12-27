from pyrogram import filters
from core.client import app
from database.users import add_user
from config.defaults import EMOJI_PROBABILITY
import random

def add_emoji(text: str) -> str:
    emojis = ["😊", "😏", "😂", "😍", "😅", "🙈", "😘"]
    if random.random() < EMOJI_PROBABILITY:
        text += f" {random.choice(emojis)}"
    return text

@app.on_message(filters.text & ~filters.edited)
def talk(_, message):
    user = message.from_user
    add_user(user.id, user.first_name)

    reply = f"Hey {user.first_name}, kya chal raha hai?"
    reply = add_emoji(reply)
    message.reply_text(reply)
