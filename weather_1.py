import requests

API_KEY = "442bc56f1271d043f53d356c728cc7e7"
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

        print(f'\nПогода в городе: {city}')
        print(f'Температура: {temp}°C')
        print(f'Описание: {description}')
        print(f'Влажность: {humidity}%')
        print(f'Скорость ветра: {wind} м/с')
    else:
        print(f'Город не найден! Проверьте название.')

city = input("Введите название города: ")
get_weather(city)