import requests
import json
from tabulate import tabulate
from styles import stylize

currency_translations = {
    'USD': 'US Dollar',
    'EUR': 'Euro',
    'PLN': 'Polish Zloty',
    'BYN': 'Belarusian Ruble',
    'CNY': 'Chinese Yuan',
    'CZK': 'Czech Koruna',
    'GBP': 'British Pound Sterling',
}


def get_exchange_data(currency_code):
    """
    Retrieves the exchange rate and currency name for a specified currency code
    from the National Bank of Ukraine (NBU) API.

    Parameters:
        currency_code (str): The three-letter currency code (e.g., 'USD', 'EUR')
        for the currency you want to get the exchange rate for.

    Returns:
        tuple or None: A tuple containing the currency name, currency code, and exchange rate as a float.
        If the currency is not found or an error occurs during the request, it returns None.

    Note:
        - The function makes an HTTP request to the NBU API to retrieve the exchange rate data.
        - The exchange rate is based on the Ukrainian hryvnia (UAH) as the base currency.
        - The NBU API provides exchange rate data for various foreign currencies.
    """
    # URL of the JSON file
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

    try:
        # Make an HTTP request to receive JSON data
        response = requests.get(url)

        # Check that the request was successful
        if response.status_code == 200:
            # Convert JSON data to Python dictionary
            data = json.loads(response.text)

            # Find the exchange rate of the hryvnia to the specified currency
            for item in data:
                if item['cc'] == currency_code:
                    return item['rate'], currency_translations.get(currency_code)

            # If currency not found, return None
            return None

        else:
            print(stylize(f"Error HTTP: {response.status_code}", "red"))
            return None

    except Exception as e:
        print(stylize(f"An error has occurred: {e}", "red"))
        return None


def exchange_rate_start():
    print(stylize("\nHere`s NBU hryvnia exchange rate to foreign currencies", "white", 'bold'))
    currencies = ['USD', 'EUR', 'PLN', 'BYN', 'CNY', 'CZK', 'GBP']
    headers = [stylize(header, "yellow", "bold") for header in ["Currency name", "Currency", "Rate"]]

    exchange_rates = []

    for currency in currencies:
        rate, currency_name = get_exchange_data(currency)
        if rate is not None:
            exchange_rates.append([stylize(currency_name, "", "bold"), stylize(currency, "green", "bold"),
                                   stylize(rate, "red", "bold")])

    colalign = ("center", "center", "center")

    table = tabulate(exchange_rates, headers, tablefmt="grid", colalign=colalign)
    print(table+"\n")


if __name__ == "__main__":
    exchange_rate_start()
