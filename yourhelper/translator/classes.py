import translators
from yourhelper.styles import stylize
from translate import Translator


"""
The latest version of the 'playsound' library can cause errors,
so you need to install an older version:

    pip install playsound==1.2.2

if you have problems installing playsound, you need to update wheel:

    pip install --upgrade wheel
"""


class TranslatorEnUk:
    """Translates text from one language to another."""

    def __init__(self, query_text: str, from_language: str, to_language: str) -> None:
        """Initialize the Translator

        Args:
            query_text (str): The text to translate.
            from_language (str): The source language code.
            to_language (str): The target language code.
        """

        self.query_text = query_text
        self.from_language = from_language
        self.to_language = to_language

        self.params = {
            'query_text': self.query_text,
            'from_language': self.from_language,
            'to_language': self.to_language,
            'update_session_after_freq': 1,
        }

    def translate(self) -> str:
        """
        Translate the text.

        Returns:
            str: The translated text.
        """

        try:
            return translators.translate_text(**self.params)
        except:
            try:
                translator = Translator(from_lang = self.from_language, to_lang=self.to_language)
                return translator.translate(self.query_text)
            except:
                return stylize("I can't translate it.", 'red')