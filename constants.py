# telegram
with open('data/token.txt', 'r') as file:
    TOKEN, CHAT_ID = [line.strip() for line in file]

# olx.ua
with open('data/locations.txt', 'r') as file:
    CITIES = [line.strip() for line in file]

EMPTY_LOCATOR = ".emptynew h1"
FOUND_LOCATOR = "#offers_table h3 a"
IMAGE_LOCATOR = "#offers_table img"
TITLE_LOCATOR = "#offers_table h3 strong"
PRICE_LOCATOR = "#offers_table p.price strong"
LOCATION_LOCATOR = '#offers_table .bottom-cell span'
OLX_HOST = "https://www.olx.ua/nedvizhimost"
FLAT = "kvartiry/dolgosrochnaya-arenda-kvartir"
HOUSE = "doma/arenda-domov"
DISTANCE = "?search%5Bdist%5D=0"
STOP_WORDS = [
    'ищу', 'ищем', 'шукаю', 'шукаємо', 'сниму', 'зніму', 'снимем',
    'знімемо', 'арендую', 'орендую', 'арендуем', 'орендуємо', 'сніму',
    'зніме', 'винайму', 'винаймемо'
]
