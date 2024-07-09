from translate import Translator


def translate_text(text, from_lang="en", to_lang="ru"):
    """Функция для перевода непонятного мне текста в процессе обучения"""
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    translation = translator.translate(text)
    return translation


if __name__ == "__main__":
    text_to_translate = "found no collectors for"
    translated_test = translate_text(text_to_translate, from_lang="en", to_lang="ru")
    print(f"Оригинальный текст: {text_to_translate}")
    print(f"Переведённый текст: {translated_test}")
