from addressbook.your_helper import main as addressbook_start
from notebook.notebook import start as notebook_start
from calculator.main_calc import main as calculator_start
from sortfolder.sortfolder import start as sortfolder_start
from translator.translator import start as translator_start
from calories_calculator import main as calories_calculator_start
from weather_forecast import main as weather_forecast_start
from currency_checker import exchange_rate_start
from styles import stylize

applications = (("Address book", addressbook_start),
                ("Notebook", notebook_start),
                ("Sort folder", sortfolder_start),
                ("Calculator", calculator_start),
                ("Exchange rate", exchange_rate_start),
                ("Translator", translator_start),
                ("Weather forecast", weather_forecast_start),
                ("Calories calculator", calories_calculator_start),
                ("Exit", ""),
                )


def main():
    while True:
        print(stylize("Welcome to YourHelper!", 'purple', 'bold'))
        print(stylize("List of available applications:", '', 'bold'))
        [print(f"{i} - {app[0]}") for i, app in enumerate(applications, 1)]
        user_input = input("Enter a number to open the application: ")

        try:
            if applications[int(user_input) - 1][0] == "Exit":
                print(stylize("Goodbye!\n", '', 'bold'))
                break
            applications[int(user_input) - 1][1]()
        except IndexError:
            print(stylize(f"Please enter a number from 1 to {len(applications)}\n", 'red'))
        except ValueError:
            print(stylize(f"Please enter a number\n", 'red'))


if __name__ == '__main__':
    main()
