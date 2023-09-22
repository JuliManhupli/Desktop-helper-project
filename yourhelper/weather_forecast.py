import requests
import json
from tabulate import tabulate
from datetime import datetime, timedelta
from yourhelper.styles import stylize

cities = [
    {"name": "Kyiv", "latitude": 50.4501, "longitude": 30.5234},
    {"name": "Kharkiv", "latitude": 49.9808, "longitude": 36.2527},
    {"name": "Odesa", "latitude": 46.4825, "longitude": 30.7233},
    {"name": "Dnipro", "latitude": 48.4647, "longitude": 35.0462},
    {"name": "Donetsk", "latitude": 48.0159, "longitude": 37.8029},
    {"name": "Zaporizhzhia", "latitude": 47.8388, "longitude": 35.1396},
    {"name": "Lviv", "latitude": 49.8397, "longitude": 24.0297},
    {"name": "Sumy", "latitude": 50.9077, "longitude": 34.7981},
    {"name": "Poltava", "latitude": 49.5883, "longitude": 34.5519},
    {"name": "Cherkasy", "latitude": 49.4444, "longitude": 32.0597},
    {"name": "Ternopil", "latitude": 49.5535, "longitude": 25.5948},
    {"name": "Uzhhorod", "latitude": 48.6208, "longitude": 22.2879},
    {"name": "Vinnytsia", "latitude": 49.2331, "longitude": 28.4682},
    {"name": "Zhytomyr", "latitude": 50.2547, "longitude": 28.6586},
    {"name": "Chernihiv", "latitude": 51.4982, "longitude": 31.2893},
    {"name": "Ivano-Frankivsk", "latitude": 48.9226, "longitude": 24.7111},
    {"name": "Kropyvnytskyi", "latitude": 48.5044, "longitude": 32.2605},
    {"name": "Luhansk", "latitude": 48.5734, "longitude": 39.3553},
    {"name": "Mykolaiv", "latitude": 46.9750, "longitude": 31.9946},
    {"name": "Poltava", "latitude": 49.5883, "longitude": 34.5519},
    {"name": "Rivne", "latitude": 50.6199, "longitude": 26.2516},
    {"name": "Sumy", "latitude": 50.9216, "longitude": 34.7981},
    {"name": "Ternopil", "latitude": 49.5535, "longitude": 25.5948},
    {"name": "Uzhhorod", "latitude": 48.6208, "longitude": 22.2879},
    {"name": "Kherson", "latitude": 46.6354, "longitude": 32.6169},
    {"name": "Cherkasy", "latitude": 49.4444, "longitude": 32.0597},
    {"name": "Chernivtsi", "latitude": 48.2917, "longitude": 25.9356},
    {"name": "Simferopol", "latitude": 44.9521, "longitude": 34.1024},
    {"name": "Sevastopol", "latitude": 44.6166, "longitude": 33.5254},
]

api_url = "https://api.open-meteo.com/v1/forecast"


def get_weather(city):
    """
        Retrieves and displays weather information for a given city.

        Args:
            city (dict): A dictionary containing information about the city. It should have the following keys:
                - 'name': The name of the city.
                - 'latitude': The latitude of the city's location.
                - 'longitude': The longitude of the city's location.

        This function makes an API request to fetch weather data for the specified city, including current weather conditions,
        hourly forecasts for today, and daily forecasts for the next three days. It then formats and prints this information
        in a user-friendly tabular format.

        Returns:
            None: This function does not return a value; it prints the weather information to the console.
    """

    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "current_weather": "true",
        "hourly": "temperature_2m,apparent_temperature,cloudcover,precipitation_probability",
        "forecast_days": 3
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        current_weather = data.get("current_weather", {})
        current_temperature = current_weather.get("temperature")
        wind_speed = current_weather.get("windspeed")

        hourly = data.get("hourly", {})
        times = hourly.get("time", [])
        temperature_2m = hourly.get("temperature_2m", [])
        apparent_temperatures = hourly.get("apparent_temperature", [])
        cloudcover = hourly.get("cloudcover", [])
        precipitation_probability = hourly.get("precipitation_probability", [])

        today = datetime.today()
        filtered_times = []
        filtered_temperature = []
        filtered_apparent_temperature = []
        filtered_cloudcover = []
        filtered_precipitation_probability = []

        for i in range(len(times)):
            time = datetime.strptime(times[i], "%Y-%m-%dT%H:%M")
            if time.date() == today.date():
                filtered_times.append(time.strftime("%H:%M"))
                filtered_temperature.append(temperature_2m[i])
                filtered_apparent_temperature.append(apparent_temperatures[i])
                filtered_cloudcover.append(cloudcover[i])
                filtered_precipitation_probability.append(precipitation_probability[i])

        colalign_hourly = ("center", "center", "center", "center", "center")
        table_hourly = [
            ["Time", "Temperature(°C)", "Apparent Temperature(°C)", "Cloud Cover(%)", "Precipitation Probability(%)"],
        ]

        for i in range(len(filtered_times)):
            table_hourly.append([filtered_times[i], filtered_temperature[i], filtered_apparent_temperature[i],
                                 filtered_cloudcover[i], filtered_precipitation_probability[i]])

        print(stylize(f"Weather forecast for {city['name']} on {today.date()} (Hourly):", '', 'bold'))
        print(tabulate(table_hourly, headers="firstrow", tablefmt="grid", colalign=colalign_hourly))

        print(stylize(f"Current Weather in {city['name']} at {today.strftime('%H:%M')}:", '', 'bold'))
        print(f"Temperature: {current_temperature}°C")
        print(f"Wind speed: {wind_speed} km/h")

        hourly = data.get("hourly", {})
        times = hourly.get("time", [])
        temperature_2m = hourly.get("temperature_2m", [])
        apparent_temperatures = hourly.get("apparent_temperature", [])

        days_data = [{"temperature": [], "apparent_temperature": []} for _ in range(3)]
        today = datetime.today()
        next_day = today + timedelta(days=1)
        for i in range(len(times)):
            time = datetime.strptime(times[i], "%Y-%m-%dT%H:%M")
            day_index = (time.date() - today.date()).days
            if 0 <= day_index < 3:
                days_data[day_index]["temperature"].append(temperature_2m[i])
                days_data[day_index]["apparent_temperature"].append(apparent_temperatures[i])

        colalign = ("center", "center", "center")
        table_daily = [
            ["Day", "Max Temperature(°C)", "Min Temperature(°C)"],
        ]

        for i, day_data in enumerate(days_data):
            date = today + timedelta(days=i + 1)
            max_temp = max(day_data["temperature"])
            min_temp = min(day_data["temperature"])
            table_daily.append([date.strftime("%Y-%m-%d"), max_temp, min_temp])

        print(stylize("\nWeather forecast for the next 3 days:", '', 'bold'))
        print(tabulate(table_daily, headers="firstrow", tablefmt="grid", colalign=colalign))

    else:
        print(f"Error fetching weather for {city['name']}")


def list_cities():
    """
        Lists the available cities for which weather information can be obtained.

        This function prints the names of cities that are available for weather information retrieval. The list of cities
        is assumed to be defined externally, and the 'cities' variable should contain a list of dictionaries, where each
        dictionary has at least the 'name' key specifying the city name.

        Returns:
            None: This function does not return a value; it prints the list of city names to the console.
    """
    print(stylize("\nList of available cities:", '', 'bold'))
    for city in cities:
        print("• " + city["name"])


def main():
    print(stylize("\nWelcome to the weather forecast!", 'white', 'bold'))
    while True:
        while True:
            print("Enter the name of a city in Ukraine or enter 'check city' to see the list of cities:")
            user_input = input(">>> ").strip().lower()

            if user_input == "check city":
                list_cities()
                continue

            selected_city = None
            for city in cities:
                if user_input == city["name"].strip().lower():
                    selected_city = city
                    break

            if selected_city:
                get_weather(selected_city)
                break
            else:
                print(stylize("City not found. Please enter a valid city name or 'check city' to see the list of "
                              "cities.", 'red'))

        while True:
            choice = input(stylize("\nDo you want to check the weather for another city? (Yes/No): ", 'yellow'))
            if choice.strip().lower() in ("no", 'n', '-'):
                print("\nThank you for using the application. Have a great day!\n")
                return
            elif choice.strip().lower() in ('yes', 'y', '+'):
                break
            else:
                print(stylize('Invalid command. Please enter "yes" or "no" to continue using the application.', 'red'))


if __name__ == '__main__':
    main()
