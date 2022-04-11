import sys
import time
from datetime import datetime

import bs4
import requests

from telegram import send_telegram
from constants import (
    CITIES, EMPTY_LOCATOR, FOUND_LOCATOR, TITLE_LOCATOR, PRICE_LOCATOR,
    IMAGE_LOCATOR, LOCATION_LOCATOR, DISTANCE, OLX_HOST, FLAT, HOUSE,
    STOP_WORDS
)


def read_data():
    with open('data.txt', 'r') as file:
        return [href[:-1] for href in file.readlines()]


def write_data(href):
    with open('data.txt', 'a') as file:
        file.write(href + '\n')


def find_in_olx(data):
    req, city = data
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print(req)
    print('\n')

    res = requests.get(req)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    if soup.select(EMPTY_LOCATOR):
        print('Нічого не знайдено!')
        print('### ### ### ### ### ### ###\n')
    else:
        hrefs = [
            link.get('href') for link in soup.select(FOUND_LOCATOR)
        ]
        images = [
            img.get('src').split(';')[0] for img in soup.select(IMAGE_LOCATOR)
        ]
        titles = [
            title.string for title in soup.select(TITLE_LOCATOR)
        ]
        prices = [
            price.string for price in soup.select(PRICE_LOCATOR)
        ]
        locations = [
            str(location)
            .replace('<span><i data-icon="location-filled"></i>', '')
            .replace('</span>', '')
            for location in soup.select(LOCATION_LOCATOR)
            if 'location-filled' in str(location)
        ]

        old_hrefs = read_data()
        hrefs_and_images = zip(hrefs, images, titles, prices, locations)

        for href_image in hrefs_and_images:
            href, image, title, price, location = href_image
            format_href = href.split('#')[0]

            if format_href not in old_hrefs:
                print(format_href)

                stop = False
                sent_status = 'false'
                for stop_word in STOP_WORDS:
                    if stop_word.lower() in title.lower():
                        stop = stop_word
                        break

                if not stop:
                    sent_status = send_telegram(
                        text=f'{location}\n{price}'
                             f'\n{title}\n\n{format_href}',
                        img=image
                    )
                else:
                    print(f'Знайдено стоп слово "{stop}" у назві "{title}"')

                if stop or sent_status:
                    write_data(format_href)


def run(city=None, hata='flat'):
    cities = CITIES
    if city in cities:
        cities = [city, ]
    elif city is not None:
        raise Exception(f'Можна вказати населений пункт зі списку: {cities}')

    if hata.lower() == 'flat':
        REQUESTS = [f"{OLX_HOST}/{FLAT}/{city}/{DISTANCE}" for city in cities]
    elif hata.lower() == 'house':
        REQUESTS = [f"{OLX_HOST}/{HOUSE}/{city}/{DISTANCE}" for city in cities]
    else:
        raise Exception('Потрібно правильно вказати тип житла: flat або house')

    while True:
        for data in zip(REQUESTS, cities):
            find_in_olx(data)
            time.sleep(30)


if __name__ == '__main__':
    city = None
    hata = 'flat'
    try:
        if len(sys.argv) > 3:
            raise Exception(
                'Можна використовувати лише два аргументи. Перший тип житла: '
                'flat або house. За замовчуванням стоїть flat. І другим '
                'аргументом можна вказати населений пункт лише у якому '
                'треба шукати!'
            )
        elif len(sys.argv) == 3:
            hata = sys.argv[1]
            city = sys.argv[2]
        elif len(sys.argv) == 2:
            hata = sys.argv[1]
        run(city=city, hata=hata)
    except Exception as e:
        print(f'{city}\n\n{e}')
