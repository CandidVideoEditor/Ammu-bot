from pyrogram import filters

# Custom filters

def is_private():
    return filters.private

def is_group():
    return filters.group

def is_text():
    return filters.text & ~filters.edited
