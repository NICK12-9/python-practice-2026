"""
Парсер погоды с Яндекс.Погода
Поддерживает: Нижний Новгород, Москва, Санкт-Петербург
Получает: текущую температуру, ощущаемую температуру, описание
"""
import requests
from bs4 import BeautifulSoup as bs4

def get_weather():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive'
    }

    city = {
    'нижний новгород': 'https://yandex.ru/pogoda/ru/nizhny-novgorod',
    'москва': 'https://yandex.ru/pogoda/ru/moscow',
    'санкт-петербург': 'https://yandex.ru/pogoda/ru/saint-petersburg'
    }

    while True:
        input_city = input('Введите город (Нижний Новгород, Москва, Санкт-Петербург): ').lower()
        if input_city in city:
            url = city[input_city]
            break
        else:
            print("Город не поддерживается. Выберите из представленных)")

    try:
        response = requests.get(url, headers= headers)
        if response.status_code == 200:
            soup = bs4(response.text, 'html.parser')
            temp = soup.find('p', 'AppFactTemperature_content__Lx4p9')
            description = soup.find('p', 'AppFact_warning__8kUUn')
            feel = soup.find('span', 'AppFact_feels__base__bw86b')
            print(f'Погода: {temp.text} {feel.text}\n{description.text}')
        else:
            print("Ошибка! Статус код не 200")
    except Exception:
        print('Ошибка!')

get_weather()