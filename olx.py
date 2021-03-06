import sys
import time
import logging

import bs4
import requests

from telegram import send_telegram
from constants import (
    EMPTY_LOCATOR, FOUND_LOCATOR, TITLE_LOCATOR, PRICE_LOCATOR,
    IMAGE_LOCATOR, LOCATION_LOCATOR, DISTANCE, OLX_HOST, FLAT, HOUSE,
    STOP_WORDS, FOUND_BLOCK_CLASS
)


logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)


def read_data(chat_id):
    with open(f'data/data_{chat_id}.txt', 'r') as file:
        return [href[:-1] for href in file.readlines()]


def write_data(href, chat_id):
    with open(f'data/data_{chat_id}.txt', 'a') as file:
        file.write(href + '\n')


def find_in_olx(requests_url, chat_id):
    logging.info(f'[olx.ua] Пошук оголошень: {requests_url}')

    olx_work = False
    for _ in range(5):

        time.sleep(1)

        res = requests.get(requests_url)
        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        soup.find()
        if ' 0 ' in soup.select(EMPTY_LOCATOR)[0]:
            logging.info('[olx.ua] Нічого не знайдено!')
            olx_work = True
            break
        elif soup.find('div', class_=FOUND_BLOCK_CLASS):
            needful_block = soup.find('div', class_=FOUND_BLOCK_CLASS)
            hrefs = [
                link.get('href') for link in
                needful_block.select(FOUND_LOCATOR)
            ]
            images = [
                img.get('src').split(';')[0] for img in
                needful_block.select(IMAGE_LOCATOR)
            ]
            titles = [
                title.string for title in needful_block.select(TITLE_LOCATOR)
            ]
            prices = [
                price.contents[0] for price in
                needful_block.select(PRICE_LOCATOR)
            ]
            locations = [
                location.contents[0] for location in
                needful_block.select(LOCATION_LOCATOR)
            ]

            old_hrefs = read_data(chat_id=chat_id)
            hrefs_and_images = zip(hrefs, images, titles, prices, locations)

            ad_found = False

            for href_image in hrefs_and_images:
                href, image, title, price, location = href_image
                format_href = href.split('#')[0]

                if format_href not in old_hrefs:
                    logging.info(
                        f'[olx.ua] Знайдено нове оголошення: {format_href}'
                    )
                    ad_found = True
                    stop = False
                    sent_status = 'false'
                    for stop_word in STOP_WORDS:
                        if stop_word.lower() in title.lower():
                            stop = stop_word
                            break

                    if not stop:
                        sent_status = send_telegram(
                            text=f'{location}\n{price}'
                                 f'\n{title}\n\nhttps://www.olx.ua'
                                 f'{format_href}',
                            img=image,
                            chat_id=chat_id,
                        )
                    else:
                        logging.info(
                            f'[olx.ua] Знайдено стоп слово "{stop}" '
                            f'у назві "{title}"'
                        )

                    if stop or sent_status:
                        write_data(href=format_href, chat_id=chat_id)
                    elif (
                            sent_status.get('error_code') == 400 and
                            sent_status.get('description') ==
                            "Bad Request: wrong file identifier/HTTP URL "
                            "specified"
                    ):
                        logging.info(
                            f'[olx.ua] Проблема з оголошенням {format_href} '
                            f'({sent_status.get("description")})'
                        )
                        write_data(href=format_href, chat_id=chat_id)
            if not ad_found:
                logging.info('[olx.ua] Нових оголошень поки що немає')
            olx_work = True
            break
        # else:
        #     raise Exception(
        #         f'Треба перевірити локатори!\n{requests_url}\n'
        #     )
    if not olx_work:
        raise Exception(
            f'Треба перевірити локатори!\n{requests_url}\n'
        )


def run(city=None, hata=None, chat_id=None):
    if hata.lower() == 'flat':
        requests_url = f"{OLX_HOST}/{FLAT}/{city}/{DISTANCE}"
    elif hata.lower() == 'house':
        requests_url = f"{OLX_HOST}/{HOUSE}/{city}/{DISTANCE}"
    else:
        raise Exception('Потрібно правильно вказати тип житла: flat або house')

    while True:
        find_in_olx(requests_url=requests_url, chat_id=chat_id)
        time.sleep(30)


if __name__ == '__main__':
    hata = sys.argv[1]
    city = sys.argv[2]
    chat_id = sys.argv[3]
    run(city=city, hata=hata, chat_id=chat_id)
