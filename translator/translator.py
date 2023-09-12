from .classes import Translator as ts, Talker as talk
from styles import stylize


def translate(from_leng: str, to_leng: str) -> None:
    """
    Translate text from one language to another.

    Args:
        from_leng (str): Source language code
        to_leng (str): Target language code

    Returns:
        None
    """

    while True:
        print('\nEnter a word or phrase to translate or enter "Back" to return to the previous menu:')
        phrase = input('>>> ')

        if phrase.lower() in ('back', "exit", "close", 'quit', 'q', '0'):
            break

        print(stylize(ts(phrase, from_leng, to_leng).translate(), "cyan"))


def say_text() -> None:
    """Speak inputted English text aloud."""

    while True:

        print('\nEnter a word or phrase in English or enter "Back" to return to the previous menu:')
        phrase = input('>>> ')

        if phrase.lower() in ('back', "exit", "close", 'quit', 'q', '0'):
            break

        talk.speak_up(phrase)


def start():
    """
    Start the translator interface.

    This function runs the main loop allowing the user to translate text
    or have English text spoken aloud.

    Returns:
        None
    """

    print(stylize("\nWelcome to the Translator!", 'white', 'bold'))

    while True:

        print(stylize('Select a command:', 'white'))
        print('1 - Translate from English to Ukrainian')
        print('2 - Translate from Ukrainian to English')
        print('3 - Listen to how a word or phrase sounds in English')
        print('4 - Return to the main menu')
        command = input('>>> ')
        if command in ('4', 'back', "exit", "close", 'quit', 'q', '0'):
            break
        elif command  == '1':
            translate('en', 'uk')
        elif command  == '2':
            translate('uk', 'en')
        elif command  == '3':
            say_text()
        else:
            print(stylize("The command is incorrect", 'red'))
