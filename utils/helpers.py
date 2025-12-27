import random

def get_random_choice(items):
    return random.choice(items) if items else None

def mention_user(user_id, name):
    return f"[{name}](tg://user?id={user_id})"
