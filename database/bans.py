from database.mongo import db

bans = db.bans

def gban(uid):
    bans.update_one({"_id": uid}, {"$set": {"gban": True}}, upsert=True)

def ungban(uid):
    bans.delete_one({"_id": uid})
