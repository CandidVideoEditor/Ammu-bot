from pyrogram import filters
from core.client import app
import random

STICKERS = ["CAACAgEAAxkBAAEBH2Fg0kK...", "CAACAgIAAxkBAAEBH3Fg0l0..."] # Add your sticker IDs

@app.on_message(filters.text & ~filters.edited)
def send_random_sticker(_, message):
    if random.random() < 0.2:  # 20% chance to send sticker
        message.reply_sticker(random.choice(STICKERS))
