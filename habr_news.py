import json

import requests
from bs4 import BeautifulSoup as bs4

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 YaBrowser/25.12.0.0 Safari/537.36',
    'accept': '*/*'
}

url = 'https://habr.com/ru/feed/'
news_data = []
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = bs4(response.text, 'lxml')
    article_all = soup.find_all('article', 'tm-articles-list__item')
    for article in article_all:
        title_all = article.find('a', "tm-title__link")
        if title_all:
            title = title_all.find('span').text
            link = 'https://habr.com' + title_all['href']

            news_data.append({
                'title': title,
                'link': link
            })
else:
    print('Ошибка статус код != 200')

if news_data:
    with open('habr_news.json', 'w', encoding='utf-8') as file:
        json.dump(news_data, file, ensure_ascii=False, indent=2)
    print(f"Загружено {len(news_data)} новостей в файл \'habr_news.json\'")
else:
    print('\nНовости не найдены')
