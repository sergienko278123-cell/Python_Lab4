from googletrans import Translator, LANGUAGES

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = Translator()
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        result = translator.detect(text)
        if set == "lang":
            return result.lang
        elif set == "confidence":
            return str(result.confidence)
        else:
            return f"Мова: {result.lang}, Надійність: {result.confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    try:
        lang = lang.lower()
        if lang in LANGUAGES:
            return LANGUAGES[lang].capitalize()
        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                return code
        return "Помилка: мову не знайдено"
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        lines = []
        lines.append(f"{'N':<5} {'Language':<20} {'ISO-639 code':<15} {'Text'}")
        lines.append("-" * 60)
        
        for i, (code, lang) in enumerate(LANGUAGES.items(), 1):
            # Щоб не чекати вічність, текст перекладаємо тільки якщо він переданий
            translated_text = ""
            if text and i <= 5: # Обмеження до 5 мов для швидкості тестування
                try:
                    translator = Translator()
                    res = translator.translate(text, dest=code)
                    translated_text = res.text
                except:
                    translated_text = "Помилка"
            elif text:
                translated_text = "..."
                
            lines.append(f"{i:<5} {lang.capitalize():<20} {code:<15} {translated_text}")
            
        result_str = "\n".join(lines)
        
        if out == "file":
            with open("languages_gtrans3.txt", "w", encoding="utf-8") as f:
                f.write(result_str)
        else:
            print(result_str)
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"

# ==========================================
# ГОЛОВНИЙ БЛОК (САМЕ ВІН ЗАПУСКАЄ ПРОГРАМУ)
# ==========================================
if __name__ == "__main__":
    print("--- Тестування модуля gtrans3 ---")
    
    txt = "Привіт, як твої справи?"
    print(f"\nОригінал: {txt}")
    print(f"Визначена мова: {LangDetect(txt, 'all')}")
    
    print(f"\nПереклад на англійську:")
    print(TransLate(txt, 'uk', 'en'))
    
    print(f"\nПеревірка коду мови:")
    print(f"Код для 'ukrainian': {CodeLang('ukrainian')}")
    
    print("\nВиведення списку мов (перші кілька з перекладом):")
    LanguageList("screen", "Привіт")