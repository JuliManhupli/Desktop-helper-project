from datetime import datetime
from .classes import Note, Notebook


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_input(prompt, error_message=None):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            if error_message:
                print(f"{bcolors.FAIL}{error_message}{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Field cannot be empty.{bcolors.ENDC}")
        else:
            return user_input


def get_tags_input():
    print(f"{bcolors.WARNING}To leave the field empty, enter '-'{bcolors.ENDC}")
    tags_input = get_input("Enter the tags separated by a comma: ", "Field cannot be empty.")
    if tags_input == "-":
        return None
    else:
        tags = [tag.strip() for tag in tags_input.lower().split(',')]
        tags = [tag.split()[0].capitalize() + ' ' + ' '.join(tag.split()[1:]) for tag in sorted(tags)]
        return tags


def get_date_input():
    print(f"{bcolors.WARNING}To leave the field empty, enter '-'{bcolors.ENDC}")
    while True:
        d_day = get_input("Enter the D-Day (YYYY-MM-DD): ", "Field cannot be empty.")
        if d_day == "-":
            return None
        try:
            date_obj = datetime.strptime(d_day, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            print(f"{bcolors.FAIL}Invalid D-Day date format. Use YYYY-MM-DD.{bcolors.ENDC}")


def add_note() -> str:
    title = get_input("Enter the title: ")
    text = get_input("Enter the note text: ")
    tags = get_tags_input()
    d_day = get_date_input()

    current_datetime = datetime.now()
    data_creation = current_datetime.strftime('%Y-%m-%d')
    note = Note(data_creation, title, text, tags, d_day)
    NOTEBOOK.add_note(note)
    return f"Note '{title}' was saved\n"


def edit_note() -> str:
    print(f"{bcolors.WARNING}To exit enter '-'{bcolors.ENDC}")
    while True:
        title = get_input("Enter the title of the note you want to edit: ")

        if title == "-":
            return "Exiting edit function.\n"

        found_note = NOTEBOOK.get(title)

        if not found_note:
            print(f"Note '{title}' not found in the notebook.")
        else:
            edit_title = get_input("Do you want to change the title? (yes/no): ").lower()
            if edit_title in ["yes", "+", "y"]:
                new_title = get_input("Enter the new title: ")
                found_note.title = new_title

            edit_text = get_input("Do you want to change the text? (yes/no): ").lower()
            if edit_text in ["yes", "+", "y"]:
                new_text = get_input("Enter the new text: ")
                found_note.text = new_text

            edit_tags = get_input("Do you want to change the tags? (yes/no): ").lower()
            if edit_tags in ["yes", "+", "y"]:
                new_tags = get_tags_input()
                found_note.tags = new_tags

            edit_d_day = get_input("Do you want to change the D-Day? (yes/no): ").lower()
            if edit_d_day in ["yes", "+", "y"]:
                new_d_day = get_date_input()
                found_note.d_day = new_d_day

            NOTEBOOK.save_to_json('notebook/notebook.json')
            return f"Note '{title}' edited successfully.\n"


def delete_note() -> str:
    print(f"{bcolors.WARNING}To exit enter '-'{bcolors.ENDC}")
    while True:
        title = get_input("Enter the title of the note you want to delete: ")
        if title == "-":
            return "Exiting delete function.\n"

        found_note = NOTEBOOK.get(title)

        if not found_note:
            print(f"Note '{title}' not found in the notebook.")
        else:
            NOTEBOOK.delete_note(found_note)
            return f"Note '{title}' deleted successfully.\n"


def sort_note() -> str:
    print("!!!")
    NOTEBOOK.sort_notes("date")
    NOTEBOOK.sort_notes("name")

    return "Notes have been sorted.\n"


def command_parser(raw_str: str):
    elements = raw_str.split()
    if len(elements) < 1:
        return f"{bcolors.FAIL}Invalid command format.{bcolors.ENDC}"

    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key()
    return "Unknown command"


COMMANDS = {
    add_note: ["add", "+", "1"],
    edit_note: ["edit", "change", "4"],
    delete_note: ["delete", "-", "5"],
    sort_note: ["sort", "sorting", "6"],
    #
    # search_note: ["search note"],
    # search_tag: ["add note"],
}


def main():
    print(f"\nWelcome to the {bcolors.BOLD}notebook{bcolors.ENDC}!")

    while True:
        print(f"{bcolors.BOLD}Available commands:{bcolors.ENDC}")
        print("1. add - Add a new note")
        print("2. search - Search for a note")
        print("3. list - List all notes")
        print("4. edit - Edit a note")
        print("5. delete - Delete a note")
        print("6. sort - Sort notes")
        print("7. menu - Exit the program\n")
        user_input = input("Enter a command: ").strip()

        if user_input.lower() == "hello":
            print("How can I help you?")

        elif user_input in ["show all", "show", "list", "3"]:
            NOTEBOOK.show_all()

        elif user_input.lower() in ["menu", "back", "7"]:
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
