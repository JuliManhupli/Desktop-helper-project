import curses


def color(text: str, status: str = 'c') -> str:
    """Adds color to the text based on the status.

    Args:
        text (str): The text to color.
        status (str): The status of the text. Defaults to 'c'.
            h - heading;
            r - required;
            o - optional;
            c - command.

    Returns:
        str: The colored text.
    """

    match status:
        case 'h':
            text = '\033[1m' + text + '\033[0m'
        case 'r':
            text = '\033[31m' + text + '\033[0m'
        case 'o':
            text = '\033[3m\033[34m' + text + '\033[0m'
        case 'c':
            text = '\033[32m' + text + '\033[0m'

    return text