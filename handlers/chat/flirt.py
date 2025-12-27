import random
from handlers.chat.languages import get_lang_data

def flirty_reply(user_name, lang="en"):
    data = get_lang_data(lang)
    replies = data.get("flirty", ["Hey {name}, tum bahut cute ho 😏"])
    return random.choice(replies).replace("{name}", user_name)
