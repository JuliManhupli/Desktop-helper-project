from styles import stylize
import requests

try:
    from calc import Calculator
except ModuleNotFoundError:
    from .calc import Calculator
'''
Start the calculator application.
# python3 -m calculator.main_calc
'''


def start_calc():
    while True:
        try:
            input_1 = float(input("Enter the first number: "))
            input_2 = float(input("Enter the second number: "))
            break
        except:
            print(stylize('The entered is not numbers', 'red'))
    print(stylize(f"The entered first and second numbers are :{input_1}, {input_2}", "green"))
    my_instance = Calculator()

    while True:
        print("The history: ", stylize(str(my_instance.history()), 'yellow', 'bold'))
        print("1 - Addition (+)")
        print("2 - Subtraction (-)")
        print("3 - Multiplication (*)")
        print("4 - Division (/)")
        print("5 - Change your number ")
        print("0 - Exit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except:
                print(stylize('Please enter a number.\n', 'red'))

        if choice == 1:
            print("The computed addition result is: ", my_instance.sum(input_1, input_2))
        elif choice == 2:
            print("The computed subtraction result is: ", my_instance.sub(input_1, input_2))
        elif choice == 3:
            print("The computed multiplication result is: ", my_instance.mul(input_1, input_2))
        elif choice == 4:
            try:
                print("The computed division result is: ", round(my_instance.div(input_1, input_2), 3))
            except:
                print(stylize('Operation is not corrected(ZeroDivisionError)', 'red'))
        elif choice == 5:
            try:
                input_1 = float(input("Enter the first number: "))
                input_2 = float(input("Enter the second number: "))
            except:
                print('The entered is not numbers')
        elif choice == 0:
            print("")
            break
        else:
            print(stylize("Sorry, invalid choice!", 'red'))


def fact_num(num: str):
    api_url = 'http://numbersapi.com/'

    response = requests.get(api_url + num)

    if response.status_code == 200:
        print(stylize(response.text + "\n", 'green'))
    else:
        print(response.status_code)


def temperature_conversion_m():
    """

    :return:
    """
    while True:
        try:
            print("Temperature Conversion:")
            print("1 - Celsius to Fahrenheit")
            print("2 - Celsius to Kelvin")
            choice = int(input("Enter your choice (1 or 2): "))
            if choice not in [1, 2]:
                print(stylize('Please enter a valid choice (1 or 2).\n', 'red'))
                continue
            value_temperature = float(input('Enter the temperature in degrees Celsius: '))
            if choice == 1:
                result = (9 / 5) * value_temperature + 32
                unit = "degrees Fahrenheit"
            else:
                result = value_temperature + 273.15
                unit = "Kelvin"
            print(stylize(f'{value_temperature} degrees Celsius is equal to {round(result, 2)} {unit}\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for temperature.\n', 'red'))


def weight_conversion_m():
    """

    :return:
    """
    while True:
        try:
            print("Weight Conversion:")
            print("1 - Kilograms to Pounds")
            print("2 - Grams to Ounces")
            choice = int(input("Enter your choice (1 or 2): "))
            if choice not in [1, 2]:
                print(stylize('Please enter a valid choice (1 or 2).\n', 'red'))
                continue
            value_weight = float(input('Enter the weight: '))
            if choice == 1:
                result = value_weight * 2.20462
                unit_1 = "kilograms"
                unit_2 = "pounds"
            else:
                result = value_weight * 0.035274
                unit_1 = "grams"
                unit_2 = "ounces"
            print(stylize(f'{value_weight} {unit_1} is equal to {round(result, 2)} {unit_2}\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for weight.\n', 'red'))


def length_conversion_m():
    """

    :return:
    """
    while True:
        try:
            print("Length Conversion:")
            print("1 - Kilometers to Miles")
            print("2 - Meters to Yards")
            print("3 - Meters to Feet")
            print("4 - Centimeters to Inches")
            print("5 - Millimeters to Inches")
            choice = int(input("Enter your choice (1, 2, 3, 4, or 5): "))
            if choice not in [1, 2, 3, 4, 5]:
                print(stylize('Please enter a valid choice (1 to 5).\n', 'red'))
                continue
            value_length = float(input('Enter the length: '))
            if choice == 1:
                result = value_length * 0.621371
                unit_1 = "kilometers"
                unit_2 = "miles"
            elif choice == 2:
                result = value_length * 1.09361
                unit_1 = "meters"
                unit_2 = "yards"
            elif choice == 3:
                result = value_length / 0.3048
                unit_1 = "meters"
                unit_2 = "feet"
            elif choice == 4:
                result = value_length * 2.5400013716
                unit_1 = "centimeters"
                unit_2 = "inches"
            else:
                result = value_length / 0.0393701
                unit_1 = "millimeters"
                unit_2 = "inches"
            print(stylize(f'{value_length} {unit_1} is equal to {round(result, 2)} {unit_2}\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for length.\n', 'red'))


def volume_conversion_m():
    """

    :return:
    """
    while True:
        try:
            print("Volume Conversion:")
            print("1 - Liters to Gallons")
            print("2 - Liters to Pints")
            choice = int(input("Enter your choice (1 or 2): "))
            if choice not in [1, 2]:
                print(stylize('Please enter a valid choice (1 or 2).\n', 'red'))
                continue
            value_volume = float(input('Enter the volume: '))
            if choice == 1:
                result = value_volume / 3.785411784
                unit = "gallons"
            else:
                result = value_volume / 0.56826125
                unit = "pints"
            print(stylize(f'{value_volume} liters is equal to {round(result, 2)} {unit}\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for volume.\n', 'red'))


def speed_conversion_m():
    """

    :return:
    """
    while True:
        try:
            print("Speed Conversion:")
            speed = float(input("Enter the speed in miles per hour: "))
            result = speed * 1.60934
            print(stylize(f'{speed} miles per hour is equal to {round(result, 2)} kilometers per hour\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for speed.\n', 'red'))


def metric_to_non_metric_conversion():
    """

    :return:
    """
    while True:
        try:
            print(stylize("Converting from metric to non-metric", '', 'bold'))
            conversion_type = int(input('What do you want to convert?\n'
                                        '1 - Temperature\n2 - Weight\n3 - Length\n4 - Volume\n5 - Speed\n'
                                        '0 - Exit to menu\n>>> '))
            if conversion_type == 0:
                print()
                break
            elif conversion_type not in [1, 2, 3, 4, 5]:
                print(stylize('Please enter a valid choice (0 to 5).\n', 'red'))
                continue
            print()
            if conversion_type == 1:
                temperature_conversion_m()
            elif conversion_type == 2:
                weight_conversion_m()
            elif conversion_type == 3:
                length_conversion_m()
            elif conversion_type == 4:
                volume_conversion_m()
            elif conversion_type == 5:
                speed_conversion_m()
        except ValueError:
            print(stylize('Please enter a number.\n', 'red'))


def temperature_conversion_nm():
    """

    :return:
    """
    while True:
        try:
            print("Temperature Conversion:")
            print("1 - Fahrenheit to Celsius")
            print("2 - Kelvin to Celsius")
            choice = int(input("Enter your choice (1 or 2): "))
            if choice not in [1, 2]:
                print(stylize('Please enter a valid choice (1 or 2).\n', 'red'))
                continue
            value_temperature = float(input('Enter the temperature in degrees Celsius: '))
            if choice == 1:
                result = (5 / 9) * (value_temperature - 32)
                unit = "degrees Fahrenheit"
            else:
                result = value_temperature - 273.15
                unit = "degrees Kelvin"
            print(stylize(f'{value_temperature} {unit} is equal to {round(result, 2)} Celsius\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for temperature.\n', 'red'))


def weight_conversion_nm():
    """

    :return:
    """
    while True:
        try:
            print("Weight Conversion:")
            print("1 - Pounds to Kilograms")
            print("2 - Ounces to Grams")
            choice = int(input("Enter your choice (1 or 2): "))
            if choice not in [1, 2]:
                print(stylize('Please enter a valid choice (1 or 2).\n', 'red'))
                continue
            value_weight = float(input('Enter the weight: '))
            if choice == 1:
                result = value_weight * 0.453592
                unit_1 = "pounds"
                unit_2 = "kilograms"
            else:
                result = value_weight * 28.3
                unit_1 = "ounces"
                unit_2 = "grams"
            print(stylize(f'{value_weight} {unit_1} is equal to {round(result, 2)} {unit_2}\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for weight.\n', 'red'))


def length_conversion_nm():
    """

    :return:
    """
    while True:
        try:
            print("Length Conversion:")
            print("1 - Miles to Kilometers")
            print("2 - Yards to Meters")
            print("3 - Feet to Meters")
            print("4 - Inches to Centimeters")
            choice = int(input("Enter your choice (1, 2, 3, or 4): "))
            if choice not in [1, 2, 3, 4]:
                print(stylize('Please enter a valid choice (1 to 4).\n', 'red'))
                continue
            value_length = float(input('Enter the length: '))
            if choice == 1:
                result = value_length / 0.621371
                unit_1 = "miles"
                unit_2 = "kilometers"
            elif choice == 2:
                result = value_length / 0.9144
                unit_1 = "yards"
                unit_2 = "meters"
            elif choice == 3:
                result = value_length / 3.28084
                unit_1 = "feet"
                unit_2 = "meters"
            else:
                result = value_length / 0.393701
                unit_1 = "inches"
                unit_2 = "centimeters"

            print(stylize(f'{value_length} {unit_1} is equal to {round(result, 2)} {unit_2}\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for length.\n', 'red'))


def volume_conversion_nm():
    """

    :return:
    """
    while True:
        try:
            print("Volume Conversion:")
            print("1 - Gallons to Liters")
            print("2 - Pints to Liters")
            choice = int(input("Enter your choice (1 or 2): "))
            if choice not in [1, 2]:
                print(stylize('Please enter a valid choice (1 or 2).\n', 'red'))
                continue
            value_volume = float(input('Enter the volume: '))
            if choice == 1:
                result = value_volume * 3.785411784
                unit = "gallons"
            else:
                result = value_volume * 0.473176473
                unit = "pints"
            print(stylize(f'{value_volume} {unit} is equal to {round(result, 2)} liters\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for volume.\n', 'red'))


def speed_conversion_nm():
    """

    :return:
    """
    while True:
        try:
            print("Speed Conversion:")
            speed = float(input("Enter the speed in kilometers per hour: "))
            result = speed / 1.60934
            print(stylize(f'{speed} kilometers per hour is equal to {round(result, 2)} miles per hour\n', 'green'))
            break
        except ValueError:
            print(stylize('Please enter a valid number for speed.\n', 'red'))


def non_metric_to_metric_conversion():
    """

    :return:
    """
    while True:
        try:
            print(stylize("Converting from non-metric to metric", '', 'bold'))
            conversion_type = int(input('What do you want to convert?\n'
                                        '1 - Temperature\n2 - Weight\n3 - Length\n4 - Volume\n5 - Speed\n'
                                        '0 - Exit to menu\n>>> '))
            if conversion_type == 0:
                print()
                break
            elif conversion_type not in [1, 2, 3, 4, 5]:
                print(stylize('Please enter a valid choice (0 to 5).\n', 'red'))
                continue
            print()
            if conversion_type == 1:
                temperature_conversion_nm()
            elif conversion_type == 2:
                weight_conversion_nm()
            elif conversion_type == 3:
                length_conversion_nm()
            elif conversion_type == 4:
                volume_conversion_nm()
            elif conversion_type == 5:
                speed_conversion_nm()
        except ValueError:
            print(stylize('Please enter a number.\n', 'red'))


def get_menu_choice():
    """
    Get the user's choice for metric to non-metric or non-metric to metric conversion.
    """
    while True:
        try:
            print(stylize("Converter Menu:", '', 'bold'))
            var = int(input(
                '1 - For metric to non-metric conversion\n2 - For non-metric to metric conversion\n0 - Exit\n>>> '))
            print()
            if var not in [1, 2, 0]:
                print(stylize('Please enter a valid choice (0 to 2).\n', 'red'))
                continue
            return var
        except ValueError:
            print(stylize('Please enter a number.\n', 'red'))


def convert_units():
    """
    Main menu to choose between metric to non-metric or non-metric to metric conversion.
    """
    while True:
        choice = get_menu_choice()
        if choice == 1:
            metric_to_non_metric_conversion()
        elif choice == 2:
            non_metric_to_metric_conversion()
        elif choice == 0:
            print(stylize("Goodbye!\n", '', 'bold'))
            break


def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Example:
        fibonacci(6)  # Returns 8
    """
    if n < 0:
        raise ValueError("Fibonacci numbers are defined only for non-negative integers.")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev = 0
    current = 1
    for _ in range(2, n + 1):
        next_num = prev + current
        prev, current = current, next_num

    return current


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Example:
        factorial(5)  # Returns 120
    """
    if n < 0:
        raise ValueError("Factorial is defined only for non-negative integers.")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    """
    main func
    main menu

    Returns:

    """
    print(stylize("\nWelcome to the calculator!", 'white', 'bold'))

    while True:

        while True:
            print(stylize("Available commands:", '', 'bold'))
            print(
                "1 - Open calculator\n2 - Open convertor\n3 - Fibonaci\n4 - Factorial\n5 - Fact for your number\n0 - "
                "Exit")
            try:
                choice = int(input("Choose a command: "))
                break
            except:
                print(stylize('Please enter a number.\n', 'red'))

        if choice == 1:
            print()
            start_calc()
        elif choice == 2:
            print()
            convert_units()

        elif choice == 3:
            while True:
                try:
                    num = int(input('Enter your number: '))
                    if num > 10000:
                        print(stylize('This number is too big.\n', 'red'))
                        continue
                    print(stylize(str(fibonacci(num)) + "\n", 'green'))
                    break
                except:
                    print(stylize('Please enter a natural number.\n', 'red'))

        elif choice == 4:
            while True:
                try:
                    num = int(input('Enter your number: '))
                    if num > 1000:
                        print(stylize('This number is too big.\n', 'red'))
                        continue
                    print(stylize(str(factorial(num)) + "\n", 'green'))
                    break
                except:
                    print(stylize('Please enter a natural number.\n', 'red'))

        elif choice == 5:
            while True:
                try:
                    num = int(input('Enter your number: '))
                    fact_num(str(num))
                    break
                except:
                    print(stylize('Please enter an integer.\n', 'red'))
        elif choice == 0:
            print(stylize("Goodbye!\n", '', 'bold'))
            break


if __name__ == '__main__':
    main()
