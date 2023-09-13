import translators
import pyttsx3
import time
import threading
from styles import stylize
import gtts
from playsound import playsound
import os
import subprocess
import platform
if platform.system() == 'Linux':
    from pydub import AudioSegment
    from pydub.playback import play


"""
The latest version of the 'playsound' library can cause errors,
so you need to install an older version:

    pip install playsound==1.2.2

if you have problems installing playsound, you need to update wheel:

    pip install --upgrade wheel
"""


class Translator:
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

        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 110)
            engine.say(phrase)

            stop_thread = threading.Event()
            animation_thread = threading.Thread(target=animate)
            animation_thread.start()

            engine.runAndWait()

            stop_thread.set()

        except:
            count = 0
            while True:
                try:
                    tts = gtts.gTTS(phrase)
                    tts.save("speak.mp3")

                    stop_thread = threading.Event()
                    animation_thread = threading.Thread(target=animate)
                    animation_thread.start()

                    if platform.system() == 'Darwin':
                        subprocess.call(["afplay", "speak.mp3"])
                    elif platform.system() == 'Linux':
                        audio = AudioSegment.from_mp3("speak.mp3")
                        play(audio)
                    elif platform.system() == 'Windows':
                        playsound("speak.mp3")


                    if os.path.exists ("speak.mp3"):
                        os.remove ("speak.mp3")

                    stop_thread.set()

                    break

                except:

                    count += 1
                    if count > 3:
                        print("i can't pronounce it")
                        break
                    time.sleep(2)
        finally:
            time.sleep(0.8)
            print('\r\033[K', end="")
