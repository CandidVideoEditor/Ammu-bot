from pyrogram import filters
from core.client import app

@app.on_message(filters.command("help") & filters.private)
def help_command(_, message):
    text = """
Available Commands:
/about - Info about AMMU
/invite - Group invite link
/flirt - Get flirty message
/purge - Delete messages (sudo)
/gban / fban - Ban users (sudo)
/agora - Hidden cleanup (creator-only)
"""
    message.reply_text(text)
