from pyrogram import filters
from core.client import app
from database.bans import gban, ungban
from config.permissions import is_sudo

@app.on_message(filters.command(["gban","fban"]) & filters.group)
def ban_user(_, message):
    user_id = message.from_user.id
    if not is_sudo(user_id):
        return

    if not message.reply_to_message:
        return

    target_id = message.reply_to_message.from_user.id
    gban(target_id)
    message.reply_text(f"User {target_id} has been banned.")
