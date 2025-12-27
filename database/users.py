from database.mongo import db

users = db.users

def get_user(uid):
    return users.find_one({"_id": uid})

def add_user(uid, name):
    users.update_one(
        {"_id": uid},
        {"$set": {"name": name}},
        upsert=True
    )
