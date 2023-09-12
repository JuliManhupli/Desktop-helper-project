import translators
import pyttsx3
import time
import threading
import locale
from styles import stylize


class Translator:
    """Translates text from one language to another."""

    def __init__(self, query_text: str, from_language: str, to_language: str) -> str:
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
            return stylize("I can't translate it.", 'red')


class Talker:
    """Speaks text aloud."""

    @staticmethod
    def speak_up(phrase: str) -> None:
        """Speak the given phrase aloud.

        Args:
            phrase (str): The phrase to speak.
        """

        def animate() -> None:
            """Show an animation while text is being spoken."""

            animation = ["   ", ")", "))", ")))", " ))", "  )", "   "]

            while not stop_thread.is_set():
                for symbol in animation:
                    print(' \U0001F50A', end="")
                    print(symbol, end="\r")
                    time.sleep(0.1)

        engine = pyttsx3.init()
        engine.setProperty("rate", 110)
        engine.setProperty("voice", "english")
        engine.say(phrase)

        stop_thread = threading.Event()
        animation_thread = threading.Thread(target=animate)
        animation_thread.start()

        engine.runAndWait()
        stop_thread.set()
        time.sleep(0.6)
        print('\r       ', end="")
