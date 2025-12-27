from core.client import app

def delete_message(chat_id, message_id):
    """
    Silently delete a message.
    """
    try:
        app.delete_messages(chat_id, message_id)
    except:
        pass

def delete_service_messages(chat_id, limit=100):
    """
    Delete join/leave/service messages in a chat.
    """
    for msg in app.get_chat_history(chat_id, limit=limit):
        if msg.service:
            delete_message(chat_id, msg.message_id)
