"""
Script to migrate DB schema or initial setup
"""
from database.mongo import db

def migrate():
    # Example: create indexes
    db.users.create_index("name")
    db.chats.create_index("active")
    db.sudo.create_index("sudo")
    print("Database migration completed.")

if __name__ == "__main__":
    migrate()
