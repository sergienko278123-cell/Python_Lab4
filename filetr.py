import json
import os
import re
import importlib

def file_translator():
    # 1. Читання конфігурації
    with open("config.json", "r") as f:
        config = json.load(f)
    
    file_path = config["file_name"]
    target_lang = config["target_lang"]
    mod_name = config["module"]
    output_type = config["output"]
    max_sentences = config["max_sentences"]

    if not os.path.exists(file_path):
        print("Error: Source file not found.")
        return

    # 2. Інформація про файл
    size = os.path.getsize(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    chars = len(content)
    sentences = re.split(r'[.!?]\s+', content)
    num_sentences = len(sentences)

    print(f"File: {file_path}")
    print(f"Size: {size} bytes, Chars: {chars}, Total Sentences: {num_sentences}")

    # Динамічний імпорт вибраного модуля
    mod = importlib.import_module(f"translator_pkg.{mod_name}")

    # Визначення мови (беремо перший речення)
    src_lang = "uk" # Для Варіанту 8 текст українською

    # 3. Обробка речень
    text_to_translate = " ".join(sentences[:max_sentences])

    # 4. Переклад (спрощено для демонстрації, враховуючи асинхронність мода1)
    import asyncio
    if mod_name == "module1":
        result = asyncio.run(mod.TransLate(text_to_translate, "auto", target_lang))
    else:
        result = mod.TransLate(text_to_translate, "auto", target_lang)

    # 5. Вивід
    if output_type == "screen":
        print(f"\nTarget Language: {target_lang}")
        print(f"Module used: {mod_name}")
        print(f"Translation:\n{result}")
    else:
        out_file = f"{os.path.splitext(file_path)[0]}_{target_lang}.txt"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(result)
        print("Ok")

if __name__ == "__main__":
    file_translator()