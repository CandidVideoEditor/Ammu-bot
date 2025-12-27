"""
Script to create all required MongoDB indexes
"""
from database.mongo import db

def create_indexes():
    db.users.create_index("_id", unique=True)
    db.chats.create_index("_id", unique=True)
    db.sudo.create_index("_id", unique=True)
    db.bans.create_index("_id", unique=True)
    db.agora.create_index("_id", unique=True)
    print("All indexes created successfully.")

if __name__ == "__main__":
    create_indexes()
