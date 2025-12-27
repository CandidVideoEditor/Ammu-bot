from database.mongo import db

chats = db.chats

def add_chat(chat_id):
    chats.update_one({"_id": chat_id}, {"$set": {"active": True}}, upsert=True)

def remove_chat(chat_id):
    chats.delete_one({"_id": chat_id})
