import re
import pprint

def animation(text):
    """Вытягивания данных регулярными выражениями"""
    pattern = r'\s{2}(\b\w+(?:\s\w+)*\b)'
    match = re.search(pattern, text)
    text_none_space = match.group().replace('  ', '')
    dict_params  = {'sky': text_none_space}

    pattern = r'[+-]\d+\(\d+\)\s°C'
    match = re.search(pattern, text)
    dict_params['degrees'] = match.group()

    pattern = r'[↖↑↗→↘↓↙←]\s\d+\skm/h'
    match = re.search(pattern, text)
    dict_params['wind_speed'] = match.group()

    pattern = r'\d+.\d\smm'
    match = re.search(pattern,text)
    dict_params['precipitation'] = match.group()

    pattern = r'\s{2}\d+\skm\b'
    match = re.search(pattern, text)
    text_none_space = match.group().replace('  ', '')
    dict_params['visibility'] = text_none_space

    pprint.pprint(dict_params)

if __name__ == "__main__":
    animation("""Weather report: Ангарск

                Overcast
       .--.     +3(2) °C       
    .-(    ).   ← 6 km/h       
   (___.__)__)  10 km          
                0.0 mm
2025-11-13
    """)
