import requests
import json

def get_exchange_rate(currency_code):
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
                    return item['rate']

            # If currency not found, return None
            return None

        else:
            print(f"Error HTTP: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error has occurred: {e}")
        return None

if __name__ == "__main__":
    print("Here currency in NBU rate")
    currencies = ['USD', 'EUR', 'PLN', 'BYN', 'CNY', 'CZK', 'GBP']

    for currency in currencies:
        rate = get_exchange_rate(currency)
        if rate is not None:
            print(f"Ukrainian hryvnia to {currency}: {rate}")
        else:
            print(f"Course {currency} not found or an error occurred.")
