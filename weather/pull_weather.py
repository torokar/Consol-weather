import re

def pull_data_weather(text):
    """Вытягивания данных регулярными выражениями с проверками"""
    dict_data_weather = {}

    pattern = r'\b(clear|overcast|cloudy|sunny|rain|snow|partly cloudy)\b'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        weather_condition = match.group(1).lower()

        weather_map = {
            'clear': 'Clear',
            'sunny': 'Sunny',
            'overcast': 'Overcast',
            'cloudy': 'Overcast',  # cloudy → Overcast
            'partly cloudy': 'Partly Cloudy',
            'rain': 'Rain',
            'snow': 'Moderate snow'
        }

        dict_data_weather['sky'] = weather_map.get(weather_condition, 'Clear')
    else:
        dict_data_weather['sky'] = "Clear"  # значение по умолчанию

    #Температура
    pattern = r'[-+]?\d+\(\d+\)\s*°C'
    match = re.search(pattern, text)
    dict_data_weather['degrees'] = match.group() if match else "Unknown"

    #Ветер
    pattern = r'[↖↑↗→↘↓↙←]\s*\d+\s*km/h'
    match = re.search(pattern, text)
    dict_data_weather['wind_speed'] = match.group() if match else "Unknown"

    #Осадки
    pattern = r'\d+\.\d\s*mm'
    match = re.search(pattern, text)
    dict_data_weather['precipitation'] = match.group() if match else "Unknown"

    #Видимость
    pattern = r'\b\d+\s*km\b'
    match = re.search(pattern, text)
    dict_data_weather['visibility'] = match.group() if match else "Unknown"

    return dict_data_weather