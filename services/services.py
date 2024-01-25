import pytz
from aiogram import Dispatcher, Router
from aiogram.types import Message
from environs import Env
from datetime import datetime
from data_functions.weather_data import get_weather_data


dp = Dispatcher()
env = Env()              # Создаем экземпляр класса Env
env.read_env()           # читаем файл .env и загружаем из него переменные в окружение
api_k = env('API_KEY')
router = Router()  # Инициализируем роутер уровня модуля


async def send_weather(message: Message):
    city_name = message.text
    weather_data = get_weather_data(city_name, api_k)
    if weather_data is not None:
        pressure = float(weather_data['main']['pressure']) * 0.7500637554192  # kPa * 0.7500637554192
        formatted_pressure = "{:.2f}".format(pressure)

        # country = weather_data['sys']['country']
        # Этот город находится в {pycountry.countries.get(alpha_2=country)}

        # Временные метки восхода, заката, текущего времени
        time_sunrise = datetime.utcfromtimestamp((weather_data['sys']['sunrise']) + (weather_data['timezone']))
        time_sunset = datetime.utcfromtimestamp((weather_data['sys']['sunset']) + (weather_data['timezone']))
        time_now = datetime.now(pytz.FixedOffset(int(weather_data['timezone']) // 60))

        return (f"Данные о погоде для {weather_data['name']}:\n\n"
                            f"Преимущественно {str(weather_data['weather'][0]['description'])}\n"
                            f"Температура: {str(weather_data['main']['temp'])}°C\n"
                            f"Атмосферное давление: {formatted_pressure} мм рт. ст. \n"
                            f"Скорость ветра: {(weather_data['wind']['speed'])} м/с\n"
                            f"Облачность: {(weather_data['clouds']['all'])} %\n\n"
                            f"Восход {time_sunrise.strftime('%H:%M')}\n"
                            f"Закат {time_sunset.strftime('%H:%M')}\n"
                            f"Местное время {time_now.strftime('%H:%M')}"
                            )

    else:
        return (f'Не удалось получить данные о погоде для {city_name}')
