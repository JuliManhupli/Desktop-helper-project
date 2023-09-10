from datetime import datetime
from styles import stylize

try:
    from classes import Note, Notebook
except ModuleNotFoundError:
    from .classes import Note, Notebook

sort_type = ("Date of creation in ascending order",
             "Date of creation in descending order",
             "Title in order from A to Z",
             "Title in order from Z to A",
             "Tags in ascending order",
             "Tags in descending order",
             "Tags sorted by word frequency in the list",
             "D-Day in ascending order",
             "D-Day in descending order",)

search_type = (("Date of creation", "date_of_creation"),
               ("Title", "title"),
               ("Text", "text"),
               ("Tags", "tags"),
               ("D_Day", "d_day"))


def get_input(prompt, error_message=None):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            if error_message:
                print(stylize(error_message, 'red'))
            else:
                print(stylize("Field cannot be empty.", 'red'))
        else:
            return user_input


def get_tags_input():
    print(stylize("To leave the field empty, enter '-'", 'yellow'))
    tags_input = get_input("Enter the tags separated by a comma: ")
    if tags_input == "-":
        return None
    else:
        tags = [tag.strip() for tag in tags_input.lower().split(',')]
        tags = [tag.split()[0].capitalize() + (' ' + ' '.join(tag.split()[1:]) if len(tag.split()) > 1 else '')
                for tag in sorted(tags)]
        return tags


def get_date_input(search=False):
    if not search:
        print(stylize("To leave the field empty, enter '-'", 'yellow'))
    while True:
        d_day = get_input("Enter the D-Day (YYYY-MM-DD): ")
        if d_day == "-" and not search:
            return None
        try:
            date_obj = datetime.strptime(d_day, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            print(stylize("Invalid D-Day date format. Use YYYY-MM-DD.", 'red'))


def add_note() -> str:
    title = get_input("Enter the title: ")

    if title in NOTEBOOK.data:
        print(stylize("Note with the title '{title}' already exists.", 'yellow'))
        overwrite_option = get_input("Do you want to overwrite it? (yes/no): ")
        if overwrite_option.lower() not in ["yes", "+", "y"]:
            count = 1

            while title in NOTEBOOK.data:
                title = f"{title} ({count})"
                count += 1

    text = get_input("Enter the note text: ")
    tags = get_tags_input()
    d_day = get_date_input()

    current_datetime = datetime.now()
    data_creation = current_datetime.strftime('%Y-%m-%d')
    note = Note(data_creation, title, text, tags, d_day)
    NOTEBOOK.add_note(note)
    return stylize(f"Note '{title}' was saved\n", '', 'bold')


def search_note():
    while True:
        print(stylize("To search notes by:", '', 'bold'))
        [print(f"{i} - {search[0]}") for i, search in enumerate(search_type, 1)]
        user_input = input("Enter a number: ")
        try:
            parameter = search_type[int(user_input) - 1][0]
            attribute = search_type[int(user_input) - 1][1]
            print(attribute)
            break
        except IndexError:
            print(stylize(f"Please enter a number from 1 to {len(search_type)}", 'red'))
        except ValueError:
            print(stylize(f"Please enter a number", 'red'))

    if attribute in ["date_of_creation", "d_day"]:
        parameter_to_search = get_date_input(True)
    else:
        parameter_to_search = get_input(f"Enter the {parameter.lower()} to search for: ").lower()

    if parameter_to_search is None:
        return stylize("No notes found with the specified parameter.\n", '', 'bold')

    if attribute == "tags":
        found_notes = [note for note in NOTEBOOK.data.values() if
                       note.tags and any(tag.lower() == parameter_to_search for tag in note.tags)]

    elif attribute in ["date_of_creation", "d_day"]:
        found_notes = [note for note in NOTEBOOK.data.values() if
                       getattr(note, attribute) == parameter_to_search]
    else:
        found_notes = [note for note in NOTEBOOK.data.values() if
                       getattr(note, attribute) and parameter_to_search in getattr(note, attribute).lower()]
    if found_notes:
        found_notebook = Notebook()
        for note in found_notes:
            found_notebook.add_note(note)
        found_notebook.show_all()
        return stylize("Search Results.\n", '', 'bold')
    else:
        return stylize("No notes found with the specified parameter.\n", '', 'bold')


def edit_note() -> str:
    print(stylize("To exit enter '-'", 'yellow'))
    while True:
        title = get_input("Enter the title of the note you want to edit: ")

        if title == "-":
            return stylize("Exiting edit function.\n", '', 'bold')

        found_note = NOTEBOOK.get(title)

        if not found_note:
            print(f"Note '{title}' not found in the notebook.")
        else:
            edit_title = get_input("Do you want to change the title? (yes/no): ").lower()
            if edit_title in ["yes", "+", "y"]:
                new_title = get_input("Enter the new title: ")

                if new_title in NOTEBOOK.data:
                    print(stylize("Note with the title '{title}' already exists.", 'yellow'))
                    overwrite_option = get_input("Do you want to overwrite it? (yes/no): ")
                    if overwrite_option.lower() not in ["yes", "+", "y"]:
                        count = 1

                        while new_title in NOTEBOOK.data:
                            new_title = f"{new_title} ({count})"
                            count += 1

                del NOTEBOOK.data[title]
                found_note.title = new_title
                NOTEBOOK.data[new_title] = found_note
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
            return stylize(f"Note '{title}' edited successfully.\n", '', 'bold')


def delete_note() -> str:
    print(stylize("To exit enter '-'", 'yellow'))
    while True:
        title = get_input("Enter the title of the note you want to delete: ")
        if title == "-":
            return stylize("Exiting delete function.\n", '', 'bold')

        found_note = NOTEBOOK.get(title)

        if not found_note:
            print(stylize(f"Note '{title}' not found in the notebook.", 'red'))
        else:
            NOTEBOOK.delete_note(found_note)
            return stylize(f"Note '{title}' deleted successfully.\n", '', 'bold')


def sort_note() -> str:
    while True:
        print(stylize("To sort notes by:", '', 'bold'))
        [print(f"{i} - {sort}") for i, sort in enumerate(sort_type, 1)]
        user_input = input("Enter a number: ")
        try:
            NOTEBOOK.sort_notes(sort_type[int(user_input) - 1])
            break
        except IndexError:
            print(stylize(f"Please enter a number from 1 to {len(sort_type)}", 'red'))
        except ValueError:
            print(stylize(f"Please enter a number", 'red'))
    return stylize("Notes have been sorted.\n", '', 'bold')


def command_parser(raw_str: str):
    elements = raw_str.split()
    if len(elements) < 1:
        return stylize("Invalid command format.", 'red')

    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key()
    return "Unknown command"


COMMANDS = {
    add_note: ["add", "+", "1"],
    search_note: ["search", "find", "2"],
    edit_note: ["edit", "change", "4"],
    delete_note: ["delete", "-", "5"],
    sort_note: ["sort", "sorting", "6"],
}


def main():
    print(stylize("\nWelcome to the notebook!", 'white', 'bold'))

    while True:
        print(stylize("Available commands:", '', 'bold'))
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
            print()

        elif user_input.lower() in ["menu", "back", "7"]:
            print(stylize("Goodbye!\n", '', 'bold'))
            break

        else:
            result = command_parser(user_input)
            print(result)


def start():
    global NOTEBOOK

    try:
        loaded_notebook = Notebook.load_from_json('notebook/notebook.json')

        NOTEBOOK = loaded_notebook
    except FileNotFoundError:
        NOTEBOOK = Notebook()

    try:
        main()
    finally:
        NOTEBOOK.save_to_json('notebook/notebook.json')
