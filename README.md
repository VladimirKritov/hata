
# hata - пошук житла на OLX.UA

### Сервіс який переглядає оголошення з орендою житла на olx.ua у вибраних населених пунктах та одразу надсилає нові оголошення у необхідну telegram групу

1. Необхідна машина з операційною системою Ubuntu 20.04 (18.04). Якщо машина на Windows або MacOS можна встановити VirtualBox, завантажити образ з Ubuntu і запустити сервіс на ньому (дивіться нижче)
2. Встановити Git, виконавши команду у терміналі ```sudo apt-get -y install git```
3. Клонувати проект, виконавши команду у терміналі ```git clone https://github.com/VladimirKritov/hata.git```
4. Перейти до клонованого проекту, виконавши команду у терміналі ```cd hata```
5. Встановити Docker та Docker-Compose, виконавши команду у терміналі ```sudo sh install_docker.sh```
6. Створити telegram бота та отримати токен.
   1. Через пошук у telegram знайти бота ```@BotFather```
   
   <img src="readme_images/token_01.jpg" width="240"/>
   
   2. За допомогою команди ```/newbot``` створити нового бота: <ім'я бота>_bot.
   
   <img src="readme_images/token_02.jpg" width="240"/>
   
   3. Зберегти токен після створення бота.
   
   <img src="readme_images/token_03.jpg" width="240"/>
   
7. Створити у telegram групу та додати туди створеного бота. **Обов'язково додати бота в адміністратори групи!**

<img src="readme_images/create_chat_01.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_02.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_03.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_04.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_05.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_06.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_07.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_08.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_09.jpg" width="240"/>
<br/>
<img src="readme_images/create_chat_10.jpg" width="240"/>

8. Дізнатися id групи, можна переглянути тут ```https://api.telegram.org/bot<BOT_TOKEN>/getUpdates``` (my_chat_member --> chat --> id)

<img src="readme_images/chat_id.jpg" width="320"/>

9. Виконати команду у терміналі для ініціалізації файлу конфігурації, який потрібно буде трохи виправити: ```sh init_config.sh```
10. В файлі **config.py** вказати токен бота, id групи та локації пошуку. **Можна одночасно шукати у різних локаціях та надсилати оголошення до різних груп!** Написання локацій населених пунктів необхідно брати з урла на olx.ua, вибираючи там локацію. Наприклад в https://www.olx.ua/d/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/ternopol/?currency=UAH беремо ternopol:
```commandline
TOKEN = '<bot_token>'
CHATS = {
    # Вибрані міста
    'ukraine': {
        'id': 000000000,  # <chat_id>
        'locations': [
            'chernovtsy', 'ternopol', 'ivano-frankovsk', 'kolomyya',
            'yaremche', 'sokal', 'chervonograd'
        ],
    },
    # Закарпатьска область
    'zak_region': {
        'id': 000000000,  # <chat_id>
        'locations': ['zak']
    },
    # Київ
    'kyiv': {
        'id': 000000000,  # <chat_id>
        'locations': ['kiev']
    },
}
```
Приклад:
```commandline
TOKEN = '5114004139:AAEKliiwO-MPm2PDhb5Ej5wcztBre4TGIUU'
CHATS = {
    # Вибрані міста
    'ukraine': {
        'id': 1051663062839,
        'locations': [
            'chernovtsy', 'ternopol', 'ivano-frankovsk', 'kolomyya',
            'yaremche', 'sokal', 'chervonograd'
        ],
    },
    # Закарпатьска область
    'zak_region': {
        'id': 2051663062833,
        'locations': ['zak']
    },
    # Київ
    'kyiv': {
        'id': 3051663062835,
        'locations': ['kiev']
    },
}
```
11. Виконати команду запуску у терміналі: ```sudo sh run.sh```
