import requests
from datetime import date

class Weather:
    def get_data_from_wttr(self, city):
        try:
            response = requests.get('https://wttr.in/' + city, timeout=10)
            weather_text = response.text
        except requests.exceptions.RequestException as e:
            print(f'Ошибка {e}')
            return None
        return weather_text

    def weather_now(self, weather_text):
        """Прогноз на данный момент времени"""
        weather_in_today = weather_text.index('mm')
        print(weather_text[:weather_in_today + 2] + f'\n{date.today()}\n')
        return weather_text[:weather_in_today + 2] + f'\n{date.today()}\n'

    def weather_for_next_days(self, weather_text):
        """Прогноз на несколько дней вперд"""
        index_new_days = weather_text.index('mm')
        return weather_text[index_new_days + 2:] + f'\n{date.today()}\n'

if __name__ == '__main__':
    c = Weather()
    g = c.get_data_from_wttr('Ангарск')
    c.weather_now(g)
