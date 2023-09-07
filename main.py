# from address_book.address_book import start as address_book_start
from notebook.notebook import start as notebook_start


def main():
    while True:
        user_input = input("Menu\nEnter a number to open the application\n"
                           "1 - address book\n2 - notebook\n>>> ")

        if user_input == "1":
            # address_book_start()
            print("Address Book")
        elif user_input == "2":
            notebook_start()
        elif user_input.lower() in ["good bye", "close", "exit", "end"]:
            print("Good bye!")
            break
        else:
            print("")


if __name__ == '__main__':
    main()
