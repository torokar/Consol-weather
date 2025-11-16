from pasing_weather import Weather
from choice import choice_users
from pull_weather import pull_data_weather
from animathion import animation_weather

def main():
    choice_return = choice_users()

    get_weather = Weather()

    """Выбор пользователя для получения нужных данных"""
    if choice_return[0] == 'weather_now':
        weather_is_now = get_weather.get_data_from_wttr(choice_return[1])
        weather_info_now = get_weather.weather_now(weather_is_now)
        dict_data_weather = pull_data_weather(weather_info_now)
        animation_weather(dict_data_weather)

    elif choice_return[0] == 'weather_for_next_day':
        weather_is_next = get_weather.get_data_from_wttr(choice_return[1])
        weather_info_few_days = get_weather.weather_for_next_days(weather_is_next)
        print(weather_info_few_days)


if __name__ == "__main__":
    main()