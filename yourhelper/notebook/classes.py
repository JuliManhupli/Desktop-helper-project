from collections import UserDict, Counter
from pathlib import Path
import json
from tabulate import tabulate

from yourhelper.addressbook.classes import Book


class Note:

    def __init__(self, date_of_creation, title, text, tags=None, d_day=None):
        """
        Initialize a Note object.

        :param date_of_creation: The date when the note was created.
        :param title: The title of the note.
        :param text: The text content of the note.
        :param tags: A list of tags associated with the note (optional, defaults to an empty list).
        :param d_day: An optional field representing a specific date associated with the note.
        """
        if tags is None:
            tags = []
        self.date_of_creation = date_of_creation
        self.title = title
        self.text = text
        self.tags = tags
        self.d_day = d_day

    def __str__(self):
        """
        Return a string representation of the Note object.

        :return: A string containing the title, text, and tags of the note.
        """
        return f"Title: {self.title}\nText: {self.text}\nTags: {', '.join(self.tags)}"


class Notebook(UserDict, Book):
    N = 10
    # documents_path = Path.home() / 'Documents' / "notebook.json"
    documents_path = 'yourhelper/notebook/notebook.json'

    def add_note(self, note: Note) -> None:
        """
        Add a Note object to the notebook and save the notebook to a JSON file.

        :param note: The Note object to be added to the notebook.
        """
        self.data[note.title] = note
        self.save_to_json()

    def delete_note(self, note: Note) -> None:
        """
        Add a Note object to the notebook and save the notebook to a JSON file.

        :param note: The Note object to be added to the notebook.
        """
        if note.title in self.data:
            del self.data[note.title]
            self.save_to_json()

    def show_all(self) -> None:
        """
        Display all notes in the notebook.
        """
        itr = iter(self)
        if itr:
            for chunk in itr:
                print(chunk)
        else:
            print("The notebook is empty")

    def sort_notes(self, key: str) -> str:
        """
        Sort the notes in the notebook based on the provided sorting key.

        :param key: The sorting key, e.g., 'Date of creation in ascending order'.
        :return: A string representation of the sorted notes.
        """
        if key == 'Date of creation in ascending order':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.date_of_creation)
        elif key == 'Date of creation in descending order':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.date_of_creation, reverse=True)
        elif key == 'Title in order from A to Z':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.title)
        elif key == 'Title in order from Z to A':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.title, reverse=True)

        elif key == 'Tags in order from A to Z':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.tags)
        elif key == 'Tags in order from Z to A':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.tags, reverse=True)
        elif key == 'Tags sorted by word frequency in the list':
            tag_counts = Counter(tag for note in self.data.values() for tag in note.tags)
            sorted_notes = sorted(self.data.values(), key=lambda note: sum(tag_counts[tag] for tag in note.tags),
                                  reverse=True)
        elif key == 'D-Day in ascending order':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.d_day or '')
        elif key == 'D-Day in descending order':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.d_day or '', reverse=True)
        else:
            return "Invalid sorting key."

        self.data = {note.title: note for note in sorted_notes}
        self.show_all()

    def save_to_json(self) -> None:
        """
        Save the notebook's data to a JSON file.
        """
        data = {}
        for key, note in self.data.items():
            data[key] = {
                'date_of_creation': note.date_of_creation,
                'title': note.title,
                'text': note.text,
                'tags': note.tags,
                'd_day': note.d_day
            }

        try:
            with open(Notebook.documents_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving data: {str(e)}")

    @classmethod
    def load_from_json(cls):
        """
        Load a notebook's data from a JSON file and create a Notebook object.

        :return: A Notebook object containing the loaded data.
        """
        try:
            with open(Notebook.documents_path, 'r') as file:
                # file_path = r"C:\Users\admin\Documents\notebook.json"
                # with open(file_path, 'r') as file:
                data = json.load(file)
            notebook = cls()

            for note_data in data.values():
                date_of_creation = note_data.get('date_of_creation', '')
                title = note_data.get('title', '')
                text = note_data.get('text', '')
                tags = note_data.get('tags', [])
                d_day = note_data.get('d_day', None)

                note = Note(date_of_creation, title, text, tags, d_day)
                notebook.add_note(note)
            return notebook
        except FileNotFoundError:
            print(f"File '{Notebook.documents_path}' not found.")
            return cls()

    def __iter__(self):
        """
        Initialize an iterator for the Notebook object.

        :return: The iterator object.
        """
        self.current_index = 0
        self.values = list(self.data.values())
        return self

    def __next__(self):
        """
        Iterate over the Notebook object and return a chunk of notes in tabular format.

        :return: A string representation of a chunk of notes.
        """
        if self.current_index < len(self.values):
            table_data = []
            max_text_width = 50
            for note in self.values[self.current_index:self.current_index + self.N]:
                text_parts = [note.text[i:i + max_text_width] for i in range(0, len(note.text), max_text_width)]
                text = '\n'.join(text_parts)

                row = [
                    note.date_of_creation,
                    note.title,
                    text,
                    ', '.join(tag for tag in note.tags) if note.tags else "N/A",
                    note.d_day if note.d_day else "N/A",
                ]
                table_data.append(row)

            headers = ['Date', 'Title', 'Text', 'Tags', 'D-Day']
            table = tabulate(table_data, headers, tablefmt='grid')

            self.current_index += self.N
            return table
        else:
            raise StopIteration
