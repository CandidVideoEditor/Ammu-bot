import random

EMOJIS = [
    "😊", "😏", "😂", "😍", "😅", "🙈", "😘", "😎", "😇", "😉", "🥰", "🤭", "🤩"
]

def add_emoji(text: str, probability: float = 0.7) -> str:
    """
    Add a random emoji to text based on probability.
    """
    if random.random() < probability:
        return f"{text} {random.choice(EMOJIS)}"
    return text
