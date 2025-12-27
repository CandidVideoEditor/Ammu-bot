from database.mongo import db

games = db.games

def set_game(chat_id, game_type, state):
    games.update_one(
        {"_id": chat_id},
        {"$set": {game_type: state}},
        upsert=True
    )

def get_game(chat_id, game_type):
    chat = games.find_one({"_id": chat_id})
    return chat.get(game_type) if chat else None
