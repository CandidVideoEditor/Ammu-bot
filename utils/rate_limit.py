import time

USER_LAST_CMD = {}

def check_rate_limit(user_id, cooldown=2):
    """
    Prevent spam commands: cooldown in seconds
    """
    now = time.time()
    last = USER_LAST_CMD.get(user_id, 0)
    if now - last < cooldown:
        return False
    USER_LAST_CMD[user_id] = now
    return True
