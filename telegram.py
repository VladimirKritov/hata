import requests

from constants import TOKEN, CHAT_ID


def send_telegram(text, img):
    url = (
        f'https://api.telegram.org/bot{TOKEN}/sendPhoto?'
        f'chat_id={CHAT_ID}&photo={img}&caption={text}'
    )
    r = requests.get(url)

    print('\n@@@ @@@ @@@   T E L E G R A M   @@@ @@@ @@@')
    print(r.text)
    print('@@@ @@@ @@@   T E L E G R A M   @@@ @@@ @@@\n')
    return r.json()['ok']


if __name__ == '__main__':
    send_telegram("Bot for OLX.UA")
