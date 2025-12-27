from config.creator import CREATOR_ID
from config.config import BOT_OWNER_ID, SUDO_USERS

def is_creator(uid: int) -> bool:
    return uid == CREATOR_ID

def is_owner(uid: int) -> bool:
    return uid in {CREATOR_ID, BOT_OWNER_ID}

def is_sudo(uid: int) -> bool:
    return uid == CREATOR_ID or uid == BOT_OWNER_ID or uid in SUDO_USERS
