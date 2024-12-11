from googletrans import Translator

translator = Translator()


def translate_text(text, scr_lang, target_lang):
    try:
        translated = translator.translate(text, src=scr_lang, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"Translation Error : {e}")
        return text
