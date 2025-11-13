import requests
from datetime import date

class Weather:
    def get_data_from_wttr(self, city):
        try:
            response = requests.get('https://wttr.in/' + city, timeout=10)
            weather_text = response.text
            weather_text = f'\n{date.today()}\n' + weather_text
        except requests.exceptions.RequestException as e:
            print(f'Ошибка {e}')
            return None
        return weather_text

    def weather_now(self, weather_text):
        weather_in_today = weather_text.index('mm')
        return weather_text[:weather_in_today + 2]

    def weather_for_next_days(self, weather_text):
        index_new_days = weather_text.index('mm')
        return weather_text[index_new_days + 2:]

