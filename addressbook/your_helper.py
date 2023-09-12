from tabulate import tabulate
from classes import AddressBook, Phone, Birthday, Email, Address
from styles import stylize


def main():
    while True:
        print("\nAvailable commands:")
        print("1. 'add' or '1'                    ->  Add a new contact")
        print("2. 'search' or 'find' or '2'       ->  Search for a contact")
        print("3. 'list' or 'show all' or '3'     ->  List all contacts")
        print("4. 'edit' or '4'                   ->  Edit a contact")
        print("5. 'upcoming' or 'birthday' or '5' ->  Find upcoming birthdays")
        print("6. 'delete' or '6'                 ->  Delete a contact")
        print("7. 'exit' or '7'                   ->  Exit the program\n")

        user_input = input("Enter a command: ").strip().lower()
        if user_input in ['add', '1']:
            name = input("Enter the name: ")
            if name in ab.data:
                contact = ab.data[name]
            else:
                contact = None

            phones = []
            while True:
                phone_input = input("Enter a phone number (or leave empty to finish adding phones): ")
                if not phone_input:
                    break
                normalized_phone = Phone(phone_input).value
                if normalized_phone:
                    phones.append(normalized_phone)
                else:
                    print(stylize("Invalid phone number format. Please enter a valid phone number", 'red'))

            email = input("Enter the email address: ")
            while email and not Email.validate_email(email):
                print(stylize("Invalid email address. Please enter a valid email address", 'red'))
                email = input("Enter the email address: ")

            birthday = input("Enter the birthday (YYYY-MM-DD): ")
            while birthday:
                try:
                    birthday = Birthday(birthday)
                    break
                except ValueError:
                    print(stylize("Invalid birthday date format. Use YYYY-MM-DD", 'red'))
                    birthday = input("Enter the birthday (YYYY-MM-DD): ")

            address = input("Enter the address: ")

            if contact:
                contact.phones = Phone(', '.join(phones))
                if email:
                    if Email.validate_email(email):
                        new_email = Email(email)
                        contact.email = new_email
                    else:
                        print(stylize("Invalid email address. Please enter a valid email address", 'red'))
                if birthday:
                    contact.birthday = Birthday(birthday)
                if address:
                    contact.address = Address(address)
            else:
                ab.add_contact(name, phones, email, birthday, address)
            print('Contact was added to our AddressBook!\n')
            ab.save_to_csv()

        elif user_input in ['search', '2', 'find']:
            name_to_search = input("Enter the name or phone number to search: ")
            found_contact = ab.search(name_to_search)
            if found_contact:
                print(f"\nContact found:")
                print(f"Name: {found_contact.name.value}")
                print(f"Phones: {found_contact.phones.value}")
                if found_contact.email:
                    print(f"Email: {found_contact.email.value}")
                if found_contact.birthday:
                    print(f"Birthday: {found_contact.birthday.value}")
                if found_contact.address:
                    print(f"Address: {found_contact.address}")
            else:
                print(stylize("\nContact not found.", 'yellow'))

        elif user_input in ['list', '3', 'show all']:
            table_data = []
            for contact in ab.data.values():
                row = [
                    contact.name.value,
                    contact.phones.value,
                    contact.email.value if contact.email else '',
                    contact.birthday.value if contact.birthday else '',
                    contact.address if contact.address else ''
                ]
                table_data.append(row)

            headers = ['Name', 'Phone', 'Email', 'Birthday', '  Address  ']
            colalign = ['center'] * len(headers)
            stralign = ['left'] * len(headers)
            index = None
            if '  Address  ' in headers:
                index = headers.index('  Address  ')
                stralign[index] = 'left'
            centered_headers = [f" {header} " for header in headers]
            if index is not None:
                centered_headers[
                    index] = f" {headers[index]} "
            table = tabulate(table_data, headers=centered_headers, tablefmt='grid', colalign=colalign,
                             stralign=stralign, disable_numparse=True)
            print(table)

        elif user_input in ['edit', '4']:
            name = input("Enter the name of the contact to edit: ")
            phone = input("Enter the new phone number (leave empty to keep the same): ")
            while True:
                email = input("Enter the new email address (leave empty to keep the same): ")
                if not email:
                    break
                if Email.validate_email(email):
                    break
                else:
                    print(stylize("Invalid email address. Please enter a valid email address", 'red'))
            address = input("Enter the new address (leave empty to keep the same): ")
            ab.edit_contact(name, phone, email, address)
            ab.save_to_csv()

        elif user_input in ['upcoming', '5', 'birthday']:
            days = int(input("Enter the number of days to search for upcoming birthdays: "))
            upcoming_birthdays = ab.find_upcoming_birthdays(days)
            if upcoming_birthdays:
                print(f"\nUpcoming birthdays:\n")
                for contact in upcoming_birthdays:
                    print(f"Name: {contact.name.value}")
                    print(f"Birthday: {contact.birthday.value}")
                    print(f"Days until birthday: {contact.days_until_birthday}\n")
            else:
                print(stylize("\nNo upcoming birthdays found within the specified number of days.", 'yellow'))

        elif user_input in ['delete', '6']:
            name = input("Enter the name of the contact to delete: ")
            ab.delete_contact(name)
            ab.save_to_csv()

        elif user_input in ['exit', '7']:
            ab.save_to_csv()
            print('\nAll tests passed and data saved!')
            print('Goodbye! ')
            break

        elif user_input not in ['add', 'search', 'list', 'edit', 'delete', 'exit', 'show all', 'find', 'upcoming',
                                'birthday']:
            print(stylize('You did not chose a command. Please, try again!', 'yellow'))


if __name__ == '__main__':
    ab = AddressBook('address_book_data.csv')
    main()
