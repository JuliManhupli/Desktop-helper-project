import json
from collections import UserDict


class Notebook(UserDict):
    N = 2
    def add_note(self, note):
        self.data[note.title] = note

    def save_to_json(self, filename):
        data = {}
        for key, note in self.data.items():
            data[key] = {
                'title': note.title,
                'text': note.text,
                'tags': note.tags
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
                title = note_data.get('title', '')
                text = note_data.get('text', '')
                tags = note_data.get('tags', [])
                note = Note(title, text, tags)
                notebook.add_note(note)
            return notebook
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return cls()

    def show_all(self):
        itr = iter(self)
        if itr:
            for chunk in itr:
                print(chunk)
        else:
            print("The notebook is empty")

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        values = list(self.data.values())
        start = self.current_index
        end = self.current_index + self.N
        current_chunk = values[start:end]
        self.current_index += self.N

        if len(current_chunk) > 0:
            representation_record = '-' * 84 + '\n'
            representation_record += '|{:^20}|{:^40}|{:^20}|\n'.format("Title", "Text", "Tags")
            representation_record += '-' * 84 + '\n'

            for note in current_chunk:
                tag_str = str(note.tags[0]) if note.tags else "N/A"
                representation_record += '|{:^20}|{:^40}|{:^20}|\n'.format(note.title, note.text, tag_str)

                for tag in note.tags[1:]:
                    representation_record += '|{:^20}|{:^40}|{:^20}|\n'.format("", "", tag)

                representation_record += '-' * 84 + '\n'

            return representation_record
        else:
            raise StopIteration

class Note:
    def __init__(self, title, text, tags=None):
        if tags is None:
            tags = []
        self.title = title
        self.text = text
        self.tags = tags

    def __str__(self):
        return f"Title: {self.title}\nText: {self.text}\nTags: {', '.join(self.tags)}"
