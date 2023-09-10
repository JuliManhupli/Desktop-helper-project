from styles import stylize
import requests


try:
    from calc import Calculator
except ModuleNotFoundError:
    from .calc import Calculator
'''
Start the calculator application.
'''


def start_calc():
    while True:
        try:
            input_1 = float(input("Enter the first number: "))
            input_2 = float(input("Enter the second number: "))
            break
        except:
            print(stylize('The entered is not numbers', 'red'))
    print(f"The entered first and second numbers are :{input_1}, {input_2}")
    my_instance = Calculator()
    choice = 1
    while choice != 0:
        print("The history: ", my_instance.history())
        print("0. Exit")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Change your number ")
        choice = int(input("Enter your choice... \n>>>"))
        if choice == 1:
            print("The computed addition result is : ", my_instance.sum(input_1, input_2))
        elif choice == 2:
            print("The computed subtraction result is : ", my_instance.sub(input_1, input_2))
        elif choice == 3:
            print("The computed product result is : ", my_instance.mul(input_1, input_2))
        elif choice == 4:
            print("The computed division result is : ", round(my_instance.div(input_1, input_2), 3))
        elif choice == 5:
            try:
                input_1 = float(input("Enter the first number: "))
                input_2 = float(input("Enter the second number: "))
            except:
                print('The entered is not numbers')
        # elif choice==6:
        #     print("The history: ", my_instance.history())
        elif choice == 0:
            print("Exit")
        else:
            print("Sorry, invalid choice!")



def other_vignettes():

    choice = 1
    while choice != 0:
        if choice == 1:
            print('Open calculator')
        elif choice == 2:
            print('Open convertor')
        elif choice == 3:
            print('fibonaci/factorial')
        elif choice == 4:
            try:
                num = int(input('Enter number\n>>>'))
                fact_num(str(num))
            except:
                print(stylize('try again', 'red'))
        elif choice == 5:
            print('Mamkin hacker')
        elif choice == 0:
            print('exit')


def fact_num(num: str):
    api_url = 'http://numbersapi.com/'

    response = requests.get(api_url + num)

    if response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)


def convert_units(var: int):
    """
    Converts between metric and non-metric units for various measurements.

    Args:
        var (int): 1 for metric to non-metric conversion, 2 for non-metric to metric conversion.

    Raises:
        ValueError: If an invalid choice is made.

    Example:
        convert_units(1)  # Convert metric to non-metric
    """
    # var = int(input('1: Ru - Eng\n2: Eng - Ru\n'))
    while var!=0:
        if var == 1:
            print('Converting from metric to non-metric')
            conversion_type = int(
                input('What do we convert?\n 1. Temperature\n 2. Weight\n 3. Length\n 4. Volume\n 5. Speed\n '))

            # Temperature conversion
            if conversion_type == 1:
                temperature = int(input(' 1. Celsius to Fahrenheit\n 2. Celsius to Kelvin\n'))
                if temperature == 1:
                    value_temperature = float(input('How many degrees Celsius? :\n'))
                    print(value_temperature, 'degrees Celsius is equal to',
                          round(((9 / 5) * value_temperature + 32), 2), 'degrees Fahrenheit')
                elif temperature == 2:
                    value_temperature = float(input('How many degrees Celsius? :\n'))
                    print(value_temperature, 'degrees Celsius is equal to', round((value_temperature + 273.15), 2),
                          'Kelvin')

            # Weight conversion
            elif conversion_type == 2:
                mass = int(input(' 1. Kilograms to Pounds\n 2. Grams to Ounces\n '))
                if mass == 1:
                    value_mass = float(input('How many kilograms? :\n'))
                    print(value_mass, 'kilograms is equal to', round((value_mass * 2.20462), 2), 'pounds')
                elif mass == 2:
                    value_mass = float(input('How many grams? :\n'))
                    print(value_mass, 'grams is equal to', round((value_mass * 0.035274), 2), 'ounces')

            # Length conversion
            elif conversion_type == 3:
                length = int(input(' 1. Kilometers to Miles\n 2. Meters to Yards\n 3. Meters to Feet\n '
                                   '4. Centimeters to Inches\n 5. Millimeters to Inches \n'))
                if length == 1:
                    value_length = float(input('How many kilometers? :\n'))
                    print(value_length, 'kilometers is equal to', round((value_length * 1.60934), 2), 'miles')
                elif length == 2:
                    value_length = float(input('How many meters? :\n'))
                    print(value_length, 'meters is equal to', round((value_length * 1.09361), 2), 'yards')
                elif length == 3:
                    value_length = float(input('How many meters? :\n'))
                    print(value_length, 'meters is equal to', round((value_length / 0.3048), 2), 'feet')
                elif length == 4:
                    value_length = float(input('How many centimeters? :\n'))
                    print(value_length, 'centimeters is equal to', round((value_length * 2.5400013716), 2), 'inches')
                elif length == 5:
                    value_length = float(input('How many millimeters? :\n'))
                    print(value_length, 'millimeters is equal to', round((value_length / 0.0393701), 2), 'inches')

            # Volume conversion
            elif conversion_type == 4:
                volume = int(input(' 1. Liters to Gallons\n 2. Liters to Pints\n'))
                if volume == 1:
                    value_volume = float(input('How many liters? : '))
                    print(value_volume, 'liters is equal to', round((value_volume / 3.785411784), 2), 'gallons')
                elif volume == 2:
                    value_volume = float(input('How many liters? :\n'))
                    print(value_volume, 'liters is equal to', round((value_volume / 0.56826125), 2), 'pints')
            elif conversion_type == 5:
                speed = float(input(' How many kilometers per hour? : '))
                print(speed, 'kilometers per hour is equal to', round((speed / 1.60934), 2), 'miles per hour')

        elif var == 2:
            print('Converting from non-metric to metric')
            conversion_type = int(
                input('What do we convert?\n 1. Temperature\n 2. Weight\n 3. Length\n 4. Volume\n 5. Speed\n '))

            # Temperature conversion
            if conversion_type == 1:
                temperature = int(input(' 1. Fahrenheit to Celsius\n 2. Kelvin to Celsius\n'))
                if temperature == 1:
                    value_temperature = float(input('How many degrees Fahrenheit? :\n'))
                    print(value_temperature, 'degrees Fahrenheit = ', round(((5 / 9) * value_temperature - 32), 2),
                          ' degrees Celsius')
                elif temperature == 2:
                    value_temperature = float(input('How many Kelvin degrees? :\n'))
                    print(value_temperature, 'Kelvin degrees = ', value_temperature - 273.15, ' degrees Celsius')

            # Weight conversion
            if conversion_type == 2:
                mass = int(input(' 1. Pounds to Kilograms\n 2. Ounces to Grams\n'))
                if mass == 1:
                    value_mass = float(input('How many pounds? :\n'))
                    print(value_mass, 'pounds is equal to', round((value_mass * 0.453592), 2), 'kilograms')
                elif mass == 2:
                    value_mass = float(input('How many ounces? :\n'))
                    print(value_mass, 'ounces is equal to', round((value_mass * 28.3), 2), 'grams')

            # Length conversion
            if conversion_type == 3:
                length = int(input(' 1. Miles to Kilometers\n 2. Yards to Meters\n 3. Feet to Meters\n '
                                   '4. Inches to Centimeters\n'))
                if length == 1:
                    value_length = float(input('How many miles? :\n'))
                    print(value_length, 'miles =', round((value_length / 0.621371), 2), 'kilometers')
                elif length == 2:
                    value_length = float(input('How many yards? :\n'))
                    print(value_length, 'yards =', round((value_length / 0.9144), 2), 'meters')
                elif length == 3:
                    value_length = float(input('How many feet? :\n'))
                    print(value_length, 'feet =', round((value_length / 3.28084), 2), 'meters')
                elif length == 4:
                    value_length = float(input('How many inches? :\n'))
                    print(value_length, 'inches =', round((value_length / 0.393701), 2), 'centimeters')

            # Volume conversion
            if conversion_type == 4:
                volume = int(input(' 1. Gallons to Liters\n 2. Pints to Liters\n'))
                if volume == 1:
                    value_volume = float(input('How many gallons? : \n'))
                    print(value_volume, 'gallons =', round((value_volume * 3.785411784), 2), 'liters')
                if volume == 2:
                    value_volume = float(input('How many pints? : \n'))
                    print(value_volume, 'pints =', round((value_volume * 0.473176473), 2), 'liters')

            # Speed conversion
            if conversion_type == 5:
                speed = float(input('How many miles per hour? :\n'))
                print(speed, 'miles per hour =', round((speed * 1.60934), 2), 'kilometers per hour')

        elif var == 0:
            print('exit')
            break
        else:
            raise ValueError("Invalid choice. Please select either 1 or 2.")


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


if __name__ == '__main__':
    convert_units(int(input('>>')))


