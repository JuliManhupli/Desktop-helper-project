COLORS = {
    'red': 91,
    'yellow': 93,
    'green': 92,
    'cyan': 96,
    'blue': 94,
    'purple': 95,
    'gray': 90,
    'white': 97,
    'bg_red': 101,
    'bg_yellow': 103,
    'bg_green': 102,
    'bg_cyan': 106,
    'bg_blue': 104,
    'bg_purple': 105,
    'bg_gray': 100,
    'bg_white': 107
}

STYLES = {
    'bold': 1,
    'italic': 3,
    'underline': 4,
    'strikethrough': 9
}

def stylize(text: str,  color: str = '', style: str = '') -> str:

    if color:
        text = f"\033[{COLORS[color]}m{text}\033[0m"

    if style:
        text = f"\033[{STYLES[style]}m{text}\033[0m"

    return text
