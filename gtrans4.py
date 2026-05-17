import asyncio
from googletrans import Translator, LANGUAGES

translator = Translator()

async def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        res = await translator.translate(text, src=scr, dest=dest)
        return res.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

async def LangDetect(text: str, set: str = "all") -> str:
    try:
        det = await translator.detect(text)
        if set == "lang":
            return det.lang
        elif set == "confidence":
            return str(det.confidence)
        return f"Мова: {det.lang}, Довіра: {det.confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    lang_lower = lang.lower()
    if lang_lower in LANGUAGES:
        return LANGUAGES[lang_lower].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang_lower:
            return code
    return "Помилка: Невідомий код або назва мови"

async def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        header_no = "N"
        header_lang = "Language"
        header_code = "ISO-639 code"
        header_text = "Translated text"
        
        lines = []
        if text:
            lines.append(f"{header_no:<4} | {header_lang:<25} | {header_code:<15} | {header_text}")
            lines.append("-" * 80)
        else:
            lines.append(f"{header_no:<4} | {header_lang:<25} | {header_code:<15}")
            lines.append("-" * 50)

        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            if text:
                tr = await TransLate(text, "auto", code)
                lines.append(f"{i:<4} | {name.capitalize():<25} | {code:<15} | {tr}")
            else:
                lines.append(f"{i:<4} | {name.capitalize():<25} | {code:<15}")
        
        result_str = "\n".join(lines)
        
        if out == "file":
            with open("languages_gtrans4.txt", "w", encoding="utf-8") as f:
                f.write(result_str)
        else:
            print(result_str)
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"