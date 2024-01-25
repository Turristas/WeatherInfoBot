import requests
from environs import Env

env = Env()              # Создаем экземпляр класса Env
env.read_env()           # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

api_k = env('API_KEY')


def get_coordinates_data(city, api_key):
    url = "https://api.openweathermap.org/geo/1.0/direct"
    # Параметры запроса
    params = {
        'q': city,
        'limit': 5,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()  # Получение данных в формате JSON
            return data
        else:
            print("Ошибка при запросе к API. Код статуса:", response.status_code)
            print("Текст ошибки:", response.text)
            return None

    except Exception as e:
        print("Произошла ошибка:", str(e))
        return None
