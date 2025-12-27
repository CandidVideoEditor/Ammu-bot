from database.mongo import db

sudo = db.sudo

def add_sudo(uid):
    sudo.update_one({"_id": uid}, {"$set": {"sudo": True}}, upsert=True)

def remove_sudo(uid):
    sudo.delete_one({"_id": uid})
