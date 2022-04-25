import logging
import requests

from constants import TOKEN, CHAT_ID


logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)


def send_telegram(text, img):
    url = (
        f'https://api.telegram.org/bot{TOKEN}/sendPhoto?'
        f'chat_id={CHAT_ID}&photo={img}&caption={text}'
    )
    logging.info(f'[telegram] Надсилання повідомлення в telegram: {repr(url)}')
    r = requests.get(url)
    logging.info(
        f'[telegram] Результат надсилання повідомлення до telegram: {r.text}'
    )
    return r.json()


if __name__ == '__main__':
    send_telegram("Bot for OLX.UA")
