# from address_book.address_book import start as address_book_start
from notebook.notebook import start as notebook_start

applications = (("Address book", 'addressbook_start'),
                ("Notebook", notebook_start),
                # ("Sort folder", sortfolder_start),

                )


def main():
    while True:
        print("Menu", "Enter a number to open the application:", sep='\n')
        [print(f"{i} - {app[0]}") for i, app in enumerate(applications, 1)]
        user_input = input(">>> ")

        try:
            applications[int(user_input) - 1][1]()
        except IndexError:
            print(f"Please enter a number from 1 to {len(applications)}")
        except ValueError:
            print(f"Please enter a number")


if __name__ == '__main__':
    main()
