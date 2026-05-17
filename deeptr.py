from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

# Словник підтримуваних мов для deep_translator Google
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        # Обробка 'auto' для сумісності
        source_lang = 'auto' if scr == 'auto' else scr
        return GoogleTranslator(source=source_lang, target=dest).translate(text)
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = detect(text)
        if set == "lang":
            return lang
        
        # Отримання коефіцієнта довіри
        predictions = detect_langs(text)
        confidence = predictions[0].prob if predictions else 0.0
        
        if set == "confidence":
            return str(confidence)
        return f"Мова: {lang}, Довіра: {confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    lang_lower = lang.lower()
    if lang_lower in LANGUAGES:  # Якщо передано назву мови (наприклад, 'english')
        return LANGUAGES[lang_lower]
    
    # Якщо передано код мови
    for name, code in LANGUAGES.items():
        if code == lang_lower:
            return name.capitalize()
    return "Помилка: Невідомий код або назва мови"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        lines = []
        if text:
            lines.append(f"{'N':<4} | {'Language':<25} | {'ISO-639 code':<15} | {'Translated text'}")
            lines.append("-" * 80)
        else:
            lines.append(f"{'N':<4} | {'Language':<25} | {'ISO-639 code':<15}")
            lines.append("-" * 50)

        for i, (name, code) in enumerate(LANGUAGES.items(), 1):
            if text:
                tr = GoogleTranslator(source='auto', target=code).translate(text)
                lines.append(f"{i:<4} | {name.capitalize():<25} | {code:<15} | {tr}")
            else:
                lines.append(f"{i:<4} | {name.capitalize():<25} | {code:<15}")
        
        result_str = "\n".join(lines)
        
        if out == "file":
            with open("languages_deeptr.txt", "w", encoding="utf-8") as f:
                f.write(result_str)
        else:
            print(result_str)
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"