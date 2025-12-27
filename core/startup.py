from core.client import app
from core.logger import log_startup

def start_bot():
    app.start()
    log_startup()
    print("AMMU is online 💫")
    app.idle()
