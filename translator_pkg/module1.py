import asyncio
from googletrans import Translator, LANGUAGES

async def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = Translator()
        res = await translator.translate(text, src=src, dest=dest)
        return res.text
    except Exception as e:
        return str(e)

async def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        det = await translator.detect(text)
        if set == "lang": return det.lang
        if set == "confidence": return str(det.confidence)
        return f"Lang: {det.lang}, Confidence: {det.confidence}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    lang = lang.lower().strip()
    if lang in LANGUAGES: return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name == lang: return code
    return "Error: Not found"

async def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        header = f"{'N':<3} {'Language':<20} {'ISO-639':<8}"
        if text: header += f" {'Translation':<30}"
        
        lines = [header, "-" * len(header)]
        translator = Translator()
        
        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            row = f"{i:<3} {name.capitalize():<20} {code:<8}"
            if text:
                trans = await translator.translate(text, dest=code)
                row += f" {trans.text:<30}"
            lines.append(row)
        
        output = "\n".join(lines)
        if out == "screen":
            print(output)
        else:
            with open("lang_list_m1.txt", "w", encoding="utf-8") as f:
                f.write(output)
        return "Ok"
    except Exception as e:
        return str(e)