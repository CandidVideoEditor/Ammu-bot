from pyrogram import filters
from core.client import app

@app.on_message(filters.command("about") & filters.private)
def about(_, message):
    message.reply_text("I am AMMU Bot 😏💖\nMulti-language, flirty, music, admin & games bot.")
