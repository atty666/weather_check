import requests
import datetime
from aiogram import Bot, Dispatcher, types, executor
from hidden import bot_token, open_weather_token

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['Start'])
async def start (message: types.Message):
    await message.answer(f"Вітаю, {message.from_user.first_name}!\n"
                         f"У мене ви можете дізнатися інформацію про погоду у будь якому місці! \U0001F30E \n"
                         f"Вкажіть назву міста:")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        'Clear': "Ясно \U00002600",
        'Clouds': 'Хмарно \U00002601',
        'Rain': 'Дощ \U0001F4A7',
        'Drizzle': 'Дощ \U0001F4A7',
        'Thunderstorm': 'Гроза \U0001F329',
        'Snow': 'Сніг \U00002744',
        'Mist': 'Туман \U0001F32B'
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        cur_temp = data['main']['temp']

        weather_desc = data['weather'][0]['main']
        if weather_desc in code_to_smile:
            wd = code_to_smile[weather_desc]
        else:
            wd = f'\U0001F914 Не можу зрозуміти що за погода \U0001F914 !'

        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        length_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])
        await message.reply(f"~~~{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}~~~\n"
              f'Погода у місті: {city}\nТемпература {cur_temp}°C, {wd}\n'
              f'Швидкість вітру {wind} м\с\n'
              f'Вологість = {humidity}% \nТиск: {pressure} mmHg\n'
              f'Схід сонця {sunrise_timestamp}.\n'
              f'Захід сонця {sunset_timestamp}.\n'
              f'Тривалість дня: {length_day}\n'
              f'Гарного дня \U0001F4AA'
              )

    except:
        await message.reply(f"Перевірте чи правильна назва міста \U0001F643")
if __name__ == '__main__':
    executor.start_polling(dp)
    #git commit update linera