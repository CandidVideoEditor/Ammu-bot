from langdetect import detect
import json

LANG_FILES = {
    "en": "strings/en.json",
    "hi": "strings/hi.json",
    "kn": "strings/kn.json",
    "ta": "strings/ta.json",
    "te": "strings/te.json",
    "mr": "strings/mr.json",
    "kok": "strings/kok.json",
    "hinglish": "strings/hinglish.json",
    "kanglish": "strings/kanglish.json",
    "telish": "strings/telish.json"
}

def get_lang_data(lang):
    try:
        with open(LANG_FILES.get(lang, "strings/en.json"), "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"flirty": ["Hey {name}, kya haal hai?"]}

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"
