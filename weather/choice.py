import questionary

def choice_users():
    city = input('Введите город: ')
    city = city.title()
    license_type = questionary.select(
        "Выберите функцию",
        choices=[
            f'Погода на текущее время в городе {city}',
            f'Погода на ближайшие дни в городе {city}',
        ]).ask()

    if license_type == f'Погода на текущее время в городе {city}':
        return ('weather_now', city)
    elif license_type == f'Погода на ближайшие дни в городе {city}':
        return ('weather_for_next_day', city)

if __name__ == '__main__':
    choice_users()