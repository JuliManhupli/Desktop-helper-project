from collections import UserDict
from datetime import datetime
from abc import abstractmethod, ABC
import os
import re
import csv

from yourhelper.styles import stylize


class Book(ABC):

    @abstractmethod
    def show_all(self):
        pass


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    """
        Represents a phone number field.

        Attributes:
        value (str): The normalized phone number value.

        Methods:
        __init__(self, value=None): Initializes a Phone instance with an optional initial value.
        add_phone(self, value): Adds a phone number to the instance.
        normalize_phone(value): Static method to normalize a phone number string.
        __str__(self): Returns the phone number as a string.
    """

    def __init__(self, value=None):
        super().__init__(value)
        if value is not None:
            self.value = self.normalize_phone(value)
        else:
            self.value = ''

    @staticmethod
    def normalize_phone(value):
        """
            Normalizes a string containing a phone number by removing all characters except digits and the '+' sign.

            Parameters:
            value (str): The string containing a phone number or other value.

            Returns:
            str: The normalized string containing only digits and the '+' sign.

        """
        if isinstance(value, str):
            return re.sub(r'[^\d+\-]+', '', value)
        else:
            return value

    def add_phone(self, value):
        """
            Adds a phone number to the existing phone number(s) of this Phone instance.

            Args:
            value (str): The phone number to add.
        """
        normalized_value = self.normalize_phone(value)
        if self.value:
            self.value += ', '
        self.value += normalized_value

    def __str__(self):
        """
            Returns the phone number as a string.

            Returns:
            str: The phone number value as a string.
        """
        return self.value


class Email(Field):
    """
        Represents an email address field.

        Attributes:
        value (str): The email address value.

        Methods:
        __init__(self, value): Initializes an Email instance with an initial value.
        validate_email(email): Static method to validate an email address.
        """

    def __init__(self, value):
        super().__init__(value)
        self.value = self.validate_email(value)

    @staticmethod
    def validate_email(email):
        """
             Validates an email address.

             Args:
             email (str): The email address to validate.

             Returns:
             str: The valid email address or None if it's not valid.
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return email


class Birthday(Field):
    """
        Represents a birthday field.

        Attributes:
        value (str): The normalized birthday value in 'YYYY-MM-DD' format.

        Methods:
        __init__(self, value): Initializes a Birthday instance with an initial value.
        normalize_birthday(value): Static method to normalize a birthday string.
        """

    def __init__(self, value):
        super().__init__(value)
        self.value = self.normalize_birthday(value)

    @staticmethod
    def normalize_birthday(value):
        """
            Normalizes a birthday string to 'YYYY-MM-DD' format.

            Args:
            value (str): The birthday string to normalize.

            Returns:
            str: The normalized birthday string.

            Raises:
            ValueError: If the input is not in the 'YYYY-MM-DD' format.
        """
        try:
            date_obj = datetime.strptime(value, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            raise ValueError(stylize("Invalid birthday date format. Use YYYY-MM-DD", 'red'))


class Address(Field):
    """
        Represents an address field.

        Methods:
        __str__(self): Returns the address as a string.
        """

    def __str__(self):
        return self.value


class Record:
    """
        Represents a contact record.

        Attributes:
        name (Name): The name of the contact.
        phones (Phone): The phone numbers associated with the contact.
        email (Email): The email address of the contact.
        birthday (Birthday): The birthday of the contact.
        address (Address): The address of the contact.

        Methods:
        add_phone(self, phone): Adds a phone number to the contact.
        get_phones(self): Returns a string with the contact's phone numbers.
        """

    def __init__(self, name, birthday=None, address=None):
        self.name = name
        self.phones = Phone()
        self.email = None
        self.birthday = birthday
        self.address = address

    def add_phone(self, phone):
        """
            Adds a phone number to the contact's phone numbers.

            Args:
            phone (str): The phone number to add.
        """
        self.phones.add_phone(phone)

    def get_phones(self):
        """
            Returns a string with the contact's phone numbers.

            Returns:
            str: A string containing the contact's phone numbers.
        """
        return self.phones.value if self.phones.value else 'No phone numbers'


class AddressBook(UserDict, Book):
    """
        Represents an address book for storing and managing contact records.

        Attributes:
        file (str): The path to the CSV file used to store contacts.

        Methods:
        __init__(self, file_path): Initializes the address book with a specified CSV file.
        create_csv_file(self): Creates a new CSV file if it doesn't exist.
        save_to_csv(self): Saves the contact records to the CSV file.
        load_from_csv(self): Loads contact records from the CSV file.
        add_contact(self, name, phones=None, email=None, birthday=None, address=None): Adds a new contact.
        delete_contact(self, name): Deletes a contact by name.
        edit_contact(self, name, phone=None, email=None, address=None): Edits a contact's information.
        search(self, query): Searches for a contact based on a query.
        find_upcoming_birthdays(self, days): Finds contacts with upcoming birthdays within a specified number of days.
        """

    def __init__(self, file_path):
        super().__init__()
        self.file = file_path
        if not os.path.exists(self.file):
            self.create_csv_file()
        self.load_from_csv()

    def create_csv_file(self):
        """
            Creates a new CSV file for storing contacts.

            Example of usage:
            address_book.create_csv_file()
        """
        with open(self.file, 'w', encoding='utf-8', newline='') as file:
            field_names = ['Name', 'Phone', 'Email', 'Birthday', 'Address']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
        print(f'Created a new CSV file: {self.file}')

    def save_to_csv(self):
        """
            Saves the contact records to the CSV file.

            Example of usage:
            address_book.save_to_csv()
        """
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
        """
            Loads contact records from the CSV file.

            Example of usage:
            address_book.load_from_csv()
        """
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
                    print(stylize(f"Contact '{name}' already exists!", 'yellow'))

    def add_contact(self, name, phones=None, email=None, birthday=None, address=None):
        """
            Adds a new contact to the address book.

            Args:
            name (str): The name of the contact.
            phones (str or list, optional): The phone number(s) of the contact.
            email (str, optional): The email address of the contact.
            birthday (str or Birthday, optional): The birthday of the contact.
            address (str or Address, optional): The address of the contact.
        """
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
                    print(stylize("Invalid email address. Please enter a valid email address", 'red'))
                    return

            while birthday:
                try:
                    birthday = birthday.value
                    birthday = Birthday(birthday)
                    break
                except ValueError:
                    print(stylize("Invalid birthday date format. Use YYYY-MM-DD", 'red'))
                    birthday = input("Enter the birthday (YYYY-MM-DD): ")

            self.data[name] = new_contact
        else:
            print(stylize("Contact already exists!", 'yellow'))
        self.save_to_csv()

    def delete_contact(self, name):
        """
            Deletes a contact from the address book by name.

            Args:
            name (str): The name of the contact to delete.
        """
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found in the address book.")
        self.save_to_csv()

    def edit_contact(self, name, phone=None, email=None, address=None):
        """
            Edits a contact's information.

            Args:
            name (str): The name of the contact to edit.
            phone (str, optional): The new phone number of the contact.
            email (str, optional): The new email address of the contact.
            address (str, optional): The new address of the contact.
        """
        if name in self.data:
            contact = self.data[name]

            if phone:
                contact.phones = Phone(phone)
            if email:
                if Email.validate_email(email):
                    new_email = Email(email)
                    contact.email = new_email
                else:
                    print(stylize("Invalid email address.", 'red'))
            if address:
                contact.address = Address(address)

            print(f"Contact '{name}' edited successfully.")
        else:
            print(f"Contact '{name}' not found in the address book.")
        self.save_to_csv()

    def search(self, query):
        """
        Searches for a contact based on a query.

        Args:
        query (str): The query to search for in contact names or phone numbers.

        Returns:
        Record: The contact record that exactly matches the query or None if no match is found.
        """

        exact_matches = []

        for record in self.data.values():
            if query.lower() == record.name.value.lower():
                return record
            else:
                for phone in record.phones.value.split(', '):
                    if query == phone:
                        exact_matches.append(record)

        if len(exact_matches) == 1:
            return exact_matches[0]
        elif len(exact_matches) > 1:
            print(stylize("Multiple exact matches found. Please provide a more specific query.", 'yellow'))
            return None

        return None

    def find_upcoming_birthdays(self, days):
        """
            Finds contacts with upcoming birthdays within a specified number of days.

            Args:
            days (int): The number of days to consider for upcoming birthdays.

            Returns:
            list: A list of contacts with upcoming birthdays, sorted by days until the birthday.
        """
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

    def show_all(self):
        return self.data.values()