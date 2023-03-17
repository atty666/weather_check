import requests
import datetime
import random
from hidden import open_weather_token
from pprint import pprint

good_days = ['good day', 'perfect day', 'nice day', 'great day']
random_day = random.choice(good_days)

def get_weather (city, open_weather_token):

    code_to_smile = {
        'Clear': "Clear \U00002600",
        'Clouds': 'Cloudy \U00002601',
        'Rain': 'Rain \U0001F4A7',
        'Drizzle': 'Rain \U0001F4A7',
        'Thunderstorm': 'Thunderstorm \U0001F329',
        'Snow': 'Snow \U00002744',
        'Mist': 'Fog \U0001F32B'
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        #pprint(data)

        city = data['name']
        cur_temp = data['main']['temp']

        weather_desc = data ['weather'][0]['main']
        if weather_desc in code_to_smile:
            wd = code_to_smile[weather_desc]
        else:
            wd = 'Look out the window, i cant understand whats there!'

        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        length_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        print(f"~~~{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}~~~\n"
            f'Weather in city: {city}\nTemperature {cur_temp}°C, {wd}\n'
            f'Wind speed {wind} ms\n'
            f'Humidity = {humidity}% \nPressure: {pressure} mmHg\n'
            f'Sunrise at {sunrise_timestamp}.\n'
            f'Sunset at {sunset_timestamp}.\n'
            f'Day length: {length_day}\n'
            f'Have a {random_day}!'
              )

    except Exception as ex:
        print(ex)
        print("Check the correctness of the data")


def main ():
    city = input("Where do you want to see the weather? ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()