import translators
import pyttsx3
import time
import threading
from styles import stylize


class Translator:

    def __init__(self, query_text, from_language, to_language) -> None:
        self.query_text = query_text
        self.from_language = from_language
        self.to_language = to_language

        self.params = {
            'query_text': self.query_text,
            'from_language': self.from_language,
            'to_language': self.to_language,
            'update_session_after_freq' : 1,
        }

    def translate(self):
        try:
            return translators.translate_text(**self.params)
        except:
            return stylize("I can't translate it.", 'red')


class Talker:

    @staticmethod
    def speak_up(phrase):

        def animate():

            animation = ["   ", ")", " ))", ")))", " ))", "  )", "   "]

            while not stop_thread.is_set():
                for symbol in animation:
                    print(' \U0001F50A', end="")
                    print(symbol, end="\r")
                    time.sleep(0.1)

        engine = pyttsx3.init()
        engine.setProperty("rate", 110)
        engine.say(phrase)

        stop_thread = threading.Event()
        animation_thread = threading.Thread(target=animate)
        animation_thread.start()

        engine.runAndWait()
        stop_thread.set()
        time.sleep(0.6)
        print('\r       ', end="")
