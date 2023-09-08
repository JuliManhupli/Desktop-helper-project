from collections import UserDict
import os
from datetime import datetime, timedelta
import re
import csv


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)
        if value is not None:
            self.value = self.normalize_phone(value)
        else:
            self.value = ''

    @staticmethod
    def normalize_phone(value):
        if isinstance(value, str):
            normalized_value = re.sub(r'[^0-9+]', '', value)
            return normalized_value
        else:
            return value

    def add_phone(self, value):
        normalized_value = self.normalize_phone(value)
        if self.value:
            self.value += ', '
        self.value += normalized_value

    def __str__(self):
        return self.value


class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = self.validate_email(value)

    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return email


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = self.normalize_birthday(value)

    @staticmethod
    def normalize_birthday(value):
        try:
            date_obj = datetime.strptime(value, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid birthday date format. Use YYYY-MM-DD.")


class Address(Field):
    def __str__(self):
        return self.value


class Record:
    def __init__(self, name, birthday=None, address=None):
        self.name = name
        self.phones = Phone()
        self.email = None
        self.birthday = birthday
        self.address = address

    def add_phone(self, phone):
        self.phones.add_phone(phone)

    def get_phones(self):
        return self.phones.value if self.phones.value else 'No phone numbers'


class AddressBook(UserDict):
    def __init__(self, file_path):
        super().__init__()
        self.file = file_path
        if not os.path.exists(self.file):
            self.create_csv_file()
        self.load_from_csv()

    def create_csv_file(self):
        with open(self.file, 'w', encoding='utf-8', newline='') as file:
            field_names = ['Name', 'Phone', 'Email', 'Birthday', 'Address']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
        print(f'Created a new CSV file: {self.file}')

    def save_to_csv(self):
        with open(self.file, 'w', encoding='utf-8', newline='') as file:
            field_names = ['Name', 'Phone', 'Email', 'Birthday', 'Address']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for record in self.data.values():
                row = {
                    'Name': record.name.value,
                    'Phone': record.phones.value if record.phones.value else 'No phone numbers',
                    'Email': record.email.value if isinstance(record.email, Email) else '',
                    'Birthday': record.birthday.value if isinstance(record.birthday, Birthday) else '',
                    'Address': record.address if record.address else ''
                }
                writer.writerow(row)

    def load_from_csv(self):
        if not os.path.exists(self.file):
            return
        with open(self.file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                phone = row['Phone'].split(', ')
                email = row['Email']
                birthday_str = row['Birthday']
                address = row['Address']

                birthday = None
                if birthday_str:
                    birthday = Birthday(birthday_str)

                if name not in self.data:
                    new_name = Name(name)
                    new_contact = Record(new_name, birthday, address)
                    if phone:
                        for p in phone:
                            new_contact.add_phone(p)
                    if email:
                        new_email = Email(email)
                        new_contact.email = new_email
                    self.data[name] = new_contact
                else:
                    print(f"Contact '{name}' already exists!")

    def add_contact(self, name, phones=None, email=None, birthday=None, address=None):
        if name not in self.data:
            new_name = Name(name)
            new_contact = Record(new_name, birthday, address)

            if phones:
                if isinstance(phones, list):
                    for phone in phones:
                        new_contact.add_phone(phone)
                else:
                    new_contact.add_phone(phones)

            if email:
                if Email.validate_email(email):
                    new_email = Email(email)
                    new_contact.email = new_email
                else:
                    print("Invalid email address. Please enter a valid email address.")
                    return

            while birthday:
                try:
                    birthday = birthday.value
                    birthday = Birthday(birthday)
                    break
                except ValueError:
                    print("Invalid birthday date format. Use YYYY-MM-DD.")
                    birthday = input("Enter the birthday (YYYY-MM-DD): ")

            self.data[name] = new_contact
        else:
            print("Contact already exists!")
        self.save_to_csv()

    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found in the address book.")
        self.save_to_csv()

    def edit_contact(self, name, phone=None, email=None, address=None):
        if name in self.data:
            contact = self.data[name]

            if phone:
                contact.phones = Phone(phone)
            if email:
                if Email.validate_email(email):
                    new_email = Email(email)
                    contact.email = new_email
                else:
                    print("Invalid email address.")
            if address:
                contact.address = Address(address)

            print(f"Contact '{name}' edited successfully.")
        else:
            print(f"Contact '{name}' not found in the address book.")
        self.save_to_csv()

    def search(self, query):
        for record in self.data.values():
            if query.lower() in record.name.value.lower():
                return record
            else:
                for phone in record.phones.value.split(', '):
                    if query in phone:
                        return record
        return None

    def find_upcoming_birthdays(self, days):
        today = datetime.today()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, '%Y-%m-%d')
                next_birthday_date = datetime(today.year, birthday_date.month, birthday_date.day)

                if next_birthday_date < today:
                    next_birthday_date = datetime(today.year + 1, birthday_date.month, birthday_date.day)

                days_until_birthday = (next_birthday_date - today).days
                if 0 <= days_until_birthday <= days:
                    record.days_until_birthday = days_until_birthday
                    upcoming_birthdays.append(record)

        return upcoming_birthdays

    def iterate_records(self, batch_size=10):
        records = list(self.data.values())
        for i in range(0, len(records), batch_size):
            yield records[i:i + batch_size]