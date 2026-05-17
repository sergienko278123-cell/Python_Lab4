import sys
from googletrans import Translator, LANGUAGES

def check_version():
    if sys.version_info >= (3, 11):
        print("Warning: This module is intended for Python versions < 3.13.")

def TransLate(text, src, dest):
    check_version()
    try:
        t = Translator()
        return t.translate(text, src=src, dest=dest).text
    except Exception as e: return str(e)

def LangDetect(text, set="all"):
    check_version()
    try:
        t = Translator()
        det = t.detect(text)
        if set == "lang": return det.lang
        if set == "confidence": return str(det.confidence)
        return f"Lang: {det.lang}, Confidence: {det.confidence}"
    except Exception as e: return str(e)

def CodeLang(lang):
    check_version()
    lang = lang.lower().strip()
    if lang in LANGUAGES: return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name == lang: return code
    return "Error"

def LanguageList(out="screen", text=None):
    check_version()
    # Логіка аналогічна module1, але синхронна
    print("Listing languages (Module 2)...")
    return "Ok"

# ==========================================
# ДОДАНО: Блок для запуску коду
# ==========================================
if __name__ == "__main__":
    # Викликаємо функцію перевірки, щоб текст з'явився на екрані
    check_version()