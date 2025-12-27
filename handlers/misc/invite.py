from pyrogram import filters
from core.client import app

@app.on_message(filters.command("invite") & filters.private)
def invite(_, message):
    message.reply_text("Join our group: t.me/karnatakakingskingdom")
