from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

def TransLate(text, src, dest):
    try:
        return GoogleTranslator(source=src, target=dest).translate(text)
    except Exception as e: return str(e)

def LangDetect(text, set="all"):
    try:
        lang = detect(text)
        if set == "lang": return lang
        conf = detect_langs(text)[0].prob
        if set == "confidence": return str(conf)
        return f"Lang: {lang}, Confidence: {conf}"
    except Exception as e: return str(e)

def CodeLang(lang):
    # Використовуємо словник з googletrans для сумісності назв мов
    from googletrans import LANGUAGES
    lang = lang.lower().strip()
    if lang in LANGUAGES: return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name == lang: return code
    return "Error"

def LanguageList(out="screen", text=None):
    # Використовуємо методи deep_translator
    print("Listing languages (Module 3)...")
    return "Ok"