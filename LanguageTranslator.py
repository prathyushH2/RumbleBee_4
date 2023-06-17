from googletrans import Translator

def choose_lang():
    target_lang=input('Enter the target language (e.g.,en, fr, de):')
    return target_lang

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

text_to_translate = "Hello, how are you?"
target_language = choose_lang()  # E.g., French

translated_text = translate_text(text_to_translate, target_language)
print(f"Translated text: {translated_text}")

# pip install googletrans==4.0.0-rc1
