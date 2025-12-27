from pyrogram import filters
from core.client import app
from config.permissions import is_sudo

MUTED = {}

@app.on_message(filters.command("mute") & filters.group)
def mute_user(_, message):
    user_id = message.from_user.id
    if not is_sudo(user_id):
        return

    if not message.reply_to_message:
        return

    target_id = message.reply_to_message.from_user.id
    MUTED[target_id] = True
    message.reply_text(f"User {target_id} muted.")
