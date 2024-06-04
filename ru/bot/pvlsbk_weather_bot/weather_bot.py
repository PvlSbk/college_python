# aiogram==2.23.1
import requests
import datetime
from ru.bot.conf_data import pvlsbk_weather_bot  # уникальный telegramBot token
from ru.bot.conf_data import pvlsbk_openweathermap_token  # уникальный openweathermap.org token
from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token=pvlsbk_weather_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Приветствую! Напишите название города и пришлю сводку погоду.")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={pvlsbk_openweathermap_token}&units=metric"
        )
        data = r.json()
        # pprint(data) - форматированный вывод JSON для отладки
        date_time = datetime.datetime.fromtimestamp(data['dt'])
        formatted_date_time = date_time.strftime('%H:%M %d.%m.%Y ')
        city = data['name']
        cur_temperature = data['main']['temp']
        cur_humidity = data['main']['humidity']
        cur_pressure = data['main']['pressure']
        cur_wind = data['wind']['speed']

        await message.reply(f"Погода в городе {city} на {formatted_date_time}:\n"
                            f"Температура воздуха: {cur_temperature} °C\n"
                            f"Относительная влажность воздуха: {cur_humidity}%\n"
                            f"Атмосферное давление: {cur_pressure} мм рт.ст.\n"
                            f"Скорость ветра: {cur_wind} м/с\n\n\n"
                            f"Напишите название города и пришлю сводку погоду.")

    except:
        await message.reply("Проверьте название города")


if __name__ == '__main__':
    executor.start_polling(dp)
