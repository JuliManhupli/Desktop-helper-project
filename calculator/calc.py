class Calculator:

    history_array: list[str] = None  # Class variable to store the history of operations

    def __init__(self) -> None:
        self.history_array = []  # Initialize an empty list to store operation history for each instance

    last_operation: str | None = None  # Class variable to store the last operation performed


    @property
    def last(self) -> str | None:
        """
        Property method to retrieve the last operation performed.

        Returns:
            str | None: The last operation in string format, or None if no operations have been performed.
        """
        return Calculator.last_operation


    def sum(self, a: float, b: float) -> float:
        """
        Perform addition operation and add it to the history.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the addition.
        """
        result = a + b
        self.history_array.append(f'sum({a}, {b}) == {result}')
        Calculator.last_operation = self.history_array[-1]  # Update the last operation
        return result

    def sub(self, a: float, b: float) -> float:
        """
        Perform subtraction operation and add it to the history.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the subtraction.
        """
        result = a - b
        self.history_array.append(f'sub({a}, {b}) == {result}')
        Calculator.last_operation = self.history_array[-1]
        return result

    def mul(self, a: float, b: float) -> float:
        """
        Perform multiplication operation and add it to the history.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the multiplication.
        """
        result = a * b
        self.history_array.append(f'mul({a}, {b}) == {result}')
        Calculator.last_operation = self.history_array[-1]
        return result


    def div(self, a: float, b: float, mod: bool = False) -> float:
        """
        Perform division operation and add it to the history.

        Args:
            a (float): The dividend.
            b (float): The divisor.
            mod (bool, optional): If True, return the modulo result. Default is False.

        Returns:
            float: The result of the division.
        """
        if mod:
            result = a % b
            self.history_array.append(f'div({a}, {b}) == {result}')
        else:
            result = a / b
            self.history_array.append(f'div({a}, {b}) == {result:.3f}')


        Calculator.last_operation = self.history_array[-1]
        return result

    def pow(self, a: float, b: float) -> float:
        """
        Perform exponentiation operation and add it to the history.

        Args:
            a (float): The base.
            b (float): The exponent.

        Returns:
            float: The result of exponentiation.
        """
        result = a ** b
        self.history_array.append(f'pow({a}, {b}) == {result}')
        Calculator.last_operation = self.history_array[-1]
        return result

    def history(self) -> list[str]:
        """
        Retrieve the entire history of operations.

        Returns:
            list[str]: List of strings representing the history of operations.
        """
        return self.history_array  # Return the entire history list

    def clear(self) -> None:
        """
        Clear the last operation.
        """
        Calculator.last_operation = None  # Set the last operation to None

