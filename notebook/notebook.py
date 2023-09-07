from .classes import Note, Notebook


def add_note(title: list[str]) -> str:
    if not title:
        print("!!!")  # TODO error!

    title = ' '.join(title)

    print("Print text:")
    text = input(">>> ").strip()

    if not text:
        print("!!!")  # TODO error!

    note = Note(title, text)
    NOTEBOOK.add_note(note)
    return f"Note {title} was saved\n{note}"


def command_parser(raw_str: str):
    elements = raw_str.split()

    if len(elements) < 2:
        raise TypeError("Invalid command format: At least two elements are required.")

    for key, value in COMMANDS.items():
        if elements[0].lower() + " " + elements[1].lower() in value:
            return key(elements[2:])

    return "Unknown command"


COMMANDS = {
    add_note: ["add note"],
    # remove_note: ["remove note"],
    #
    # search_note: ["search note"],
    # search_tag: ["add note"],
}


def main():
    print(f"Notebook.\n")
    while True:
        user_input = input(">>> ").strip()

        if user_input.lower() == "hello":
            print("How can I help you?")

        elif user_input == "show all":
            NOTEBOOK.show_all()

        elif user_input.lower() in ["menu"]:
            break

        else:
            result = command_parser(user_input)
            print(result)


def start():
    global NOTEBOOK
    # ADDRESSBOOK = None
    try:
        loaded_notebook = Notebook.load_from_json('notebook/notebook.json')

        NOTEBOOK = loaded_notebook
    except FileNotFoundError:
        NOTEBOOK = Notebook()

    try:
        main()
    finally:
        NOTEBOOK.save_to_json('notebook/notebook.json')
