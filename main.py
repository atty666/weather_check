import requests
import datetime
from hidden import open_weather_token
from pprint import pprint

def get_weather (city, open_weather_token):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        #pprint(data)

        #deleted attributes
        city = data['name']
        cur_temp = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']

        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        print(f'Weather in city: {city}\nTemperature {cur_temp}°C\n'
            f'Humidity = {humidity}% \nPressure: {pressure} mmHg\n'
            f'Sunrise at {sunrise_timestamp}.\n'
            f'Sunset at {sunset_timestamp}.\n'
            f'Have a nice day!'
              )

    except Exception as ex:
        print(ex)
        print("Check the correctness of the data")


def main ():
    city = input("Where do you want to see the weather? ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()