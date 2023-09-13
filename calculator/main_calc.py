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
        print("6 - Exit")

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
        elif choice == 6:
            print("Exit\n")
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


def convert_units():
    """
    Converts between metric and non-metric units for various measurements.

    Args:

    Raises:
        ValueError: If an invalid choice is made.

    Example:
        convert_units(1)  # Convert metric to non-metric
    """

    while True:

        while True:
            try:
                print(stylize("Convertor:", '', 'bold'))
                var = int(
                    input(
                        '1 - For metric to non-metric conversion\n2 - For non-metric to metric conversion\n3 - '
                        'Exit\n>>> '))
                print()
                break
            except ValueError:
                print(stylize('Please enter a number.\n', 'red'))

            except UnboundLocalError:
                print(stylize('Please enter a number.\n', 'red'))

        if var == 1:

            while True:
                try:
                    print(stylize("Converting from metric to non-metric", '', 'bold'))
                    conversion_type = int(
                        input('What do we convert?\n1 - Temperature\n2 - Weight\n3 - Length\n4 - Volume\n'
                              '5 - Speed\n6 - Exit to menu\n>>> '))
                    if conversion_type > 6:
                        print(stylize('Please enter a number from 1 to 6.\n', 'red'))
                        continue
                    print()
                    break
                except:
                    print(stylize('Please enter a number.\n', 'red'))

            if conversion_type == 6:
                break

            # Temperature conversion
            if conversion_type == 1:

                while True:
                    try:
                        temperature = int(input('1 - Celsius to Fahrenheit\n2 - Celsius to Kelvin\n>>> '))
                        if temperature > 2:
                            print(stylize('Please enter a number 1 or 2.\n', 'red'))
                            continue
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                if temperature == 1:

                    while True:
                        try:
                            value_temperature = float(input('How many degrees Celsius: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_temperature) + ' degrees Celsius is equal to ' + \
                                 str(round(((9 / 5) * value_temperature + 32), 2)) + ' degrees Fahrenheit\n'
                    print(stylize(string_tem, 'green'))

                elif temperature == 2:

                    while True:
                        try:
                            value_temperature = float(input('How many degrees Celsius: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_temperature) + ' degrees Celsius is equal to ' + \
                                 str(round((value_temperature + 273.15), 2)) + ' degrees Kelvin\n'
                    print(stylize(string_tem, 'green'))

            # Weight conversion
            elif conversion_type == 2:

                while True:
                    try:
                        mass = int(input('1 - Kilograms to Pounds\n2 - Grams to Ounces\n>>> '))
                        if mass > 2:
                            print(stylize('Please enter a number 1 or 2.\n', 'red'))
                            continue
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                if mass == 1:
                    while True:
                        try:
                            value_mass = float(input('How many kilograms: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_mass) + ' kilograms is equal to ' + \
                                 str(round((value_mass * 2.20462), 2)) + ' pounds\n'
                    print(stylize(string_tem, 'green'))

                elif mass == 2:
                    while True:
                        try:
                            value_mass = float(input('How many grams: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_mass) + ' kilograms is equal to ' + \
                                 str(round((value_mass * 0.035274), 2)) + ' ounces\n'
                    print(stylize(string_tem, 'green'))

            # Length conversion
            elif conversion_type == 3:

                while True:
                    try:
                        length = int(input('1 - Kilometers to Miles\n2 - Meters to Yards\n3 - Meters to Feet\n'
                                           '4 - Centimeters to Inches\n5 - Millimeters to Inches\n>>> '))
                        if length > 5:
                            print(stylize('Please enter a number from 1 to 5.\n', 'red'))
                            continue
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                if length == 1:

                    while True:
                        try:
                            value_length = float(input('How many kilometers: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_length) + ' kilometers is equal to ' + \
                                 str(round((value_length * 1.60934), 2)) + ' miles\n'
                    print(stylize(string_tem, 'green'))

                elif length == 2:

                    while True:
                        try:
                            value_length = float(input('How many meters: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_length) + ' meters is equal to ' + \
                                 str(round((value_length * 1.09361), 2)) + ' yards\n'
                    print(stylize(string_tem, 'green'))

                elif length == 3:
                    while True:
                        try:
                            value_length = float(input('How many meters: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_length) + ' meters is equal to ' + \
                                 str(round((value_length / 0.3048), 2)) + ' feet\n'
                    print(stylize(string_tem, 'green'))
                elif length == 4:
                    while True:
                        try:
                            value_length = float(input('How many centimeters: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_length) + ' centimeters is equal to ' + \
                                 str(round((value_length * 2.5400013716), 2)) + ' inches\n'
                    print(stylize(string_tem, 'green'))
                elif length == 5:
                    while True:
                        try:
                            value_length = float(input('How many millimeters: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_length) + ' millimeters is equal to ' + \
                                 str(round((value_length / 0.0393701), 2)) + ' inches\n'
                    print(stylize(string_tem, 'green'))

            # Volume conversion
            elif conversion_type == 4:
                while True:
                    try:
                        volume = int(input('1 - Liters to Gallons\n2 - Liters to Pints\n>>>'))
                        if volume > 2:
                            print(stylize('Please enter a number from 1 to 2.\n', 'red'))
                            continue
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                if volume == 1:
                    while True:
                        try:
                            value_volume = float(input('How many liters: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_volume) + ' liters is equal to ' + \
                                 str(round((value_volume / 3.785411784), 2)) + ' gallons\n'
                    print(stylize(string_tem, 'green'))

                elif volume == 2:
                    while True:
                        try:
                            value_volume = float(input('How many liters: '))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    string_tem = str(value_volume) + ' liters is equal to ' + \
                                 str(round((value_volume / 0.56826125), 2)) + ' pints\n'
                    print(stylize(string_tem, 'green'))
            elif conversion_type == 5:
                while True:
                    try:
                        speed = float(input('How many kilometers per hour: '))
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                string_tem = str(speed) + ' kilometers per hour is equal to ' + \
                             str(round((speed / 1.60934), 2)) + ' miles per hour\n'
                print(stylize(string_tem, 'green'))


        elif var == 2:
            while True:
                try:
                    print(stylize("Converting from non-metric to metric", '', 'bold'))
                    conversion_type = int(
                        input('What do we convert?\n1 - Temperature\n2 - Weight\n3 - Length\n4 - Volume\n'
                              '5 - Speed\n6 - Exit to menu\n>>> '))
                    if conversion_type > 6:
                        print(stylize('Please enter a number from 1 to 6.\n', 'red'))
                        continue
                    print()
                    break
                except:
                    print(stylize('Please enter a number.\n', 'red'))

            if conversion_type == 6:
                break

            # Temperature conversion
            if conversion_type == 1:
                while True:
                    try:
                        temperature = int(input('1 - Fahrenheit to Celsius\n2 - Kelvin to Celsius\n>>>'))
                        if temperature > 2:
                            print(stylize('Please enter a number 1 or 2.\n', 'red'))
                            continue
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                if temperature == 1:
                    while True:
                        try:
                            value_temperature = float(input('How many degrees Fahrenheit? :\n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_temperature, 'degrees Fahrenheit = ', round(((5 / 9) * value_temperature - 32), 2),
                          ' degrees Celsius')
                elif temperature == 2:
                    while True:
                        try:
                            value_temperature = float(input('How many Kelvin degrees? :\n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_temperature, 'Kelvin degrees = ', value_temperature - 273.15, ' degrees Celsius')

            # Weight conversion
            if conversion_type == 2:
                while True:
                    try:
                        mass = int(input(' 1 - Pounds to Kilograms\n 2 - Ounces to Grams\n'))
                        if mass > 2:
                            print(stylize('Please enter a number 1 or 2.\n', 'red'))
                            continue
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                if mass == 1:
                    while True:
                        try:
                            value_mass = float(input('How many pounds? :\n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_mass, 'pounds is equal to', round((value_mass * 0.453592), 2), 'kilograms')
                elif mass == 2:
                    while True:
                        try:
                            value_mass = float(input('How many ounces? :\n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))
                    print(value_mass, 'ounces is equal to', round((value_mass * 28.3), 2), 'grams')

            # Length conversion
            if conversion_type == 3:
                while True:
                    try:
                        length = int(input(' 1 - Miles to Kilometers\n 2 - Yards to Meters\n 3 - Feet to Meters\n '
                                           '4 - Inches to Centimeters\n'))
                        if length > 5:
                            print(stylize('Please enter a number 1 or 2.\n', 'red'))
                            continue
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                if length == 1:
                    while True:
                        try:
                            value_length = float(input('How many miles? :\n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_length, 'miles =', round((value_length / 0.621371), 2), 'kilometers')
                elif length == 2:
                    while True:
                        try:
                            value_length = float(input('How many yards? :\n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_length, 'yards =', round((value_length / 0.9144), 2), 'meters')
                elif length == 3:
                    while True:
                        try:
                            value_length = float(input('How many feet? :\n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_length, 'feet =', round((value_length / 3.28084), 2), 'meters')
                elif length == 4:
                    while True:
                        try:
                            value_length = float(input('How many inches? :\n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_length, 'inches =', round((value_length / 0.393701), 2), 'centimeters')

            # Volume conversion
            if conversion_type == 4:
                while True:
                    try:
                        volume = int(input(' 1 - Gallons to Liters\n 2 - Pints to Liters\n'))
                        if volume > 2:
                            print(stylize('Please enter a number 1 or 2.\n', 'red'))
                            continue
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                if volume == 1:
                    while True:
                        try:
                            value_volume = float(input('How many gallons? : \n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_volume, 'gallons =', round((value_volume * 3.785411784), 2), 'liters')
                if volume == 2:
                    while True:
                        try:
                            value_volume = float(input('How many pints? : \n'))
                            break
                        except:
                            print(stylize('Please enter a number.\n', 'red'))

                    print(value_volume, 'pints =', round((value_volume * 0.473176473), 2), 'liters')

            # Speed conversion
            if conversion_type == 5:
                while True:
                    try:
                        speed = float(input('How many miles per hour? :\n'))
                        break
                    except:
                        print(stylize('Please enter a number.\n', 'red'))

                print(speed, 'miles per hour =', round((speed * 1.60934), 2), 'kilometers per hour')

        elif var == 3:
            print(stylize("Goodbye!\n", '', 'bold'))
            break
        else:
            print(stylize('Please enter a number from 1 to 3.\n', 'red'))


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
    choice = None
    while True:
        print(stylize("Available commands:", '', 'bold'))
        print(
            "1 - Open calculator\n2 - Open convertor\n3 - Fibonaci\n4 - Factorial\n5 - Fact for your number\n6 - Exit")
        try:
            choice = int(input("Choose a command: "))
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
        elif choice == 6:
            print(stylize("Goodbye!\n", '', 'bold'))
            break


if __name__ == '__main__':
    main()
