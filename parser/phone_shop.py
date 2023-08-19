import requests
from bs4 import BeautifulSoup as BS

URL = 'https://www.kivano.kg/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='item product_listbox oh')
    movies = []

    for item in items:
        movies.append(
            {

                'image': URL + item.find('div', class_='listbox_img pull-left').find('img').get('src'),
                'title': URL + item.find('a').get("href")

            }
        )
    return movies


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        movies1 = []
        for page in range(0, 1):
            html = get_html(f'https://www.kivano.kg/mobilnye-telefony', params=page)
            movies1.extend(get_data(html.text))
        return movies1
    else:
        raise Exception('Parse Error.....')

