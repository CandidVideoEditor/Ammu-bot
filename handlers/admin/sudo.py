from pyrogram import filters
from core.client import app
from database.sudo import add_sudo, remove_sudo
from config.permissions import is_creator

@app.on_message(filters.command(["addsudo","removesudo"]) & filters.private)
def manage_sudo(_, message):
    user_id = message.from_user.id
    if not is_creator(user_id):
        return

    args = message.text.split()
    if len(args) < 2:
        return

    target_id = int(args[1])
    if "add" in args[0].lower():
        add_sudo(target_id)
        message.reply_text(f"{target_id} added as sudo.")
    else:
        remove_sudo(target_id)
        message.reply_text(f"{target_id} removed from sudo.")
