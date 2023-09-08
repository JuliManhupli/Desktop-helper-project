import json
import textwrap
from collections import UserDict
from tabulate import tabulate

class Notebook(UserDict):
    N = 2
    def add_note(self, note):
        self.data[note.title] = note
        self.save_to_json('notebook/notebook.json')

    def delete_note(self, note):
        if note.title in self.data:
            del self.data[note.title]
            self.save_to_json('notebook/notebook.json')

    def show_all(self):
        itr = iter(self)
        if itr:
            for chunk in itr:
                print(chunk)
        else:
            print("The notebook is empty")

    def sort_notes(self, key):
        print("sort_notes")
        if key == 'date':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.date_of_creation)
        elif key == 'name':
            sorted_notes = sorted(self.data.values(), key=lambda note: note.title)
        else:
            return "Invalid sorting key."

        self.data = {note.title: note for note in sorted_notes}
        self.show_all()
        # self.save_to_json('notebook/notebook.json')

    def save_to_json(self, filename):
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
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving data: {str(e)}")

    @classmethod
    def load_from_json(cls, filename):
        try:
            with open(filename, 'r') as file:
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
            print(f"File '{filename}' not found.")
            return cls()



    def __iter__(self):
        self.current_index = 0
        self.values = list(self.data.values())
        return self

    def __next__(self):
        if self.current_index < len(self.values):
            table_data = []
            for note in self.values[self.current_index:self.current_index + self.N]:
                row = [
                    note.date_of_creation,
                    note.title,
                    note.text,
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

class Note:
    def __init__(self, date_of_creation, title, text, tags=None, d_day=None):
        if tags is None:
            tags = []
        self.date_of_creation = date_of_creation
        self.title = title
        self.text = text
        self.tags = tags
        self.d_day = d_day

    def __str__(self):
        return f"Title: {self.title}\nText: {self.text}\nTags: {', '.join(self.tags)}"
