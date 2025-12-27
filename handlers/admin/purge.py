from pyrogram import filters
from core.client import app
from config.permissions import is_sudo
from utils.cleaners import delete_message

MAX_PURGE = 200  # or import from defaults.py

@app.on_message(filters.command("purge") & filters.group)
def purge_messages(_, message):
    user_id = message.from_user.id
    if not is_sudo(user_id):
        return

    args = message.text.split()
    try:
        limit = int(args[1])
    except:
        limit = 10

    if limit > MAX_PURGE:
        limit = MAX_PURGE

    messages_to_delete = []
    for msg in app.get_chat_history(message.chat.id, limit=limit):
        messages_to_delete.append(msg.message_id)

    for msg_id in messages_to_delete:
        delete_message(message.chat.id, msg_id)
