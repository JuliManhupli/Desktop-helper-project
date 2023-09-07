from collections import UserDict
import os
from datetime import datetime, timedelta
import re
import csv
from tabulate import tabulate


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = self.normalize_phone(value)

    def normalize_phone(self, value):
        return re.sub(r'\D', '', value)


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

    def normalize_birthday(self, value):
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
        self.phones = []
        self.email = None
        self.birthday = birthday
        self.address = address

    def add_phone(self, phone):
        self.phones.append(phone)

    """
    -------------------------- TODO
    
    def days_to_birthday(self):
        if self.birthday:
            current_date = datetime.now().date()
            value_date = datetime.strptime(self.birthday.value, '%Y-%m-%d').date()
            celebration_birthday = value_date.replace(year=current_date.year)

            if current_date > celebration_birthday:
                celebration_birthday = value_date.replace(year=current_date.year + 1)

            days_left = (celebration_birthday - current_date).days
            return days_left
        return None
        ------------------------
"""

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
                    'Phone': ', '.join(phone.value for phone in record.phones),
                    'Email': record.email.value if isinstance(record.email, Email) else '',
                    'Birthday': record.birthday.value if isinstance(record.birthday, Birthday) else '',
                    'Address': record.address if record.address else ''
                }
                writer.writerow(row)
        print('CSV table was updated!')

    def load_from_csv(self):
        if not os.path.exists(self.file):
            return
        with open(self.file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                phone = row['Phone']
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
                        new_phone = Phone(phone)
                        new_contact.add_phone(new_phone)
                    if email:
                        new_email = Email(email)
                        new_contact.email = new_email
                    self.data[name] = new_contact
                else:
                    print(f"Contact '{name}' already exists!")

    def add_contact(self, name, phone=None, email=None, birthday=None, address=None):
        if name not in self.data:
            new_name = Name(name)
            new_contact = Record(new_name, birthday, address)
            if phone:
                new_phone = Phone(phone)
                new_contact.add_phone(new_phone)
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

    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found in the address book.")

    def edit_contact(self, name, phone=None, email=None, address=None):
        if name in self.data:
            contact = self.data[name]
            if phone:
                new_phone = Phone(phone)
                contact.phones = [new_phone]
            if email:
                if Email.validate_email(email):
                    new_email = Email(email)
                    contact.email = new_email
                else:
                    print("Invalid email address.")
            if address:
                contact.address = Address(address)  # Створення об'єкта Address
            print(f"Contact '{name}' edited successfully.")
        else:
            print(f"Contact '{name}' not found in the address book.")

    def search(self, query):
        for record in self.data.values():
            if query.lower() in record.name.value.lower():
                return record
            else:
                for phone in record.phones:
                    if query in phone.value:
                        return record
        return None

    def iterate_records(self, batch_size=10):
        records = list(self.data.values())
        for i in range(0, len(records), batch_size):
            yield records[i:i + batch_size]

def main():
    while True:
        print("\nAvailable commands:")
        print("1. add - Add a new contact")
        print("2. search - Search for a contact")
        print("3. list - List all contacts")
        print("4. edit - Edit a contact")
        print("5. delete - Delete a contact")
        print("6. exit - Exit the program\n")

        user_input = input("Enter a command: ")

        if user_input == 'add':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            while not Email.validate_email(email):
                print("Invalid email address. Please enter a valid email address.")
                email = input("Enter the email address: ")
            birthday = input("Enter the birthday (YYYY-MM-DD): ")
            while birthday:
                try:
                    birthday = Birthday(birthday)
                    break
                except ValueError:
                    print("Invalid birthday date format. Use YYYY-MM-DD.")
                    birthday = input("Enter the birthday (YYYY-MM-DD): ")
            address = input("Enter the address: ")
            ab.add_contact(name, phone, email, birthday, address)
            print(f'Contact {user_input} was added to our AddressBook!\n')

        elif user_input == 'search':
            name_to_search = input("Enter the name or phone number to search: ")
            found_contact = ab.search(name_to_search)
            if found_contact:
                print(f"\nContact found:")
                print(f"Name: {found_contact.name.value}")
                print(f"Phones: {', '.join(phone.value for phone in found_contact.phones)}")
                if found_contact.email:
                    print(f"Email: {found_contact.email.value}")
                if found_contact.birthday:
                    print(f"Birthday: {found_contact.birthday.value}")
                if found_contact.address:
                    print(f"Address: {found_contact.address}")
            else:
                print("\nContact not found.")

        elif user_input == 'list':
            table_data = []
            for contact in ab.data.values():
                row = [
                    contact.name.value,
                    ', '.join(phone.value for phone in contact.phones),
                    contact.email.value if contact.email else '}',
                    contact.birthday.value if contact.birthday else '',
                    contact.address if contact.address else ''
                ]
                table_data.append(row)
            headers = ['Name', 'Phone', 'Email', 'Birthday', 'Address']
            print(tabulate(table_data, headers, tablefmt='grid'))

        elif user_input == 'edit':
            name = input("Enter the name of the contact to edit: ")
            phone = input("Enter the new phone number (leave empty to keep the same): ")
            email = input("Enter the new email address (leave empty to keep the same): ")
            address = input("Enter the new address (leave empty to keep the same): ")
            ab.edit_contact(name, phone, email, address)

        elif user_input == 'delete':
            name = input("Enter the name of the contact to delete: ")
            ab.delete_contact(name)

        elif user_input == 'exit':
            ab.save_to_csv()
            print('All tests passed and data saved!')
            print('Goodbye! :)')
            break

        elif user_input != 'add' or 'search' or 'list' or 'edit' or 'delete' or 'exit':
            print('You did not chose a command. Please, try again :)')


if __name__ == '__main__':
    ab = AddressBook('../../PycharmProjects/assistant_bot_addressbook/address_book_data.csv')
    main()

