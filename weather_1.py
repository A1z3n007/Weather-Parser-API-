import requests

API_KEY = "YOU_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print(f'\nWeather in city: {city}')
        print(f'Temperature: {temp}°C')
        print(f'Description: {description}')
        print(f'Humidity: {humidity}%')
        print(f'Wind speed: {wind} м/с')
    else:
        print(f'City not found! Check the name.')

city = input("Enter the city name: ")
get_weather(city)
