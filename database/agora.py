from database.mongo import db

agora = db.agora

def log_agora(chat_id, message_id):
    agora.insert_one({"chat_id": chat_id, "message_id": message_id})

def get_agora_messages(chat_id, limit=100):
    return list(agora.find({"chat_id": chat_id}).sort("_id", -1).limit(limit))
