
# hata - пошук житла на OLX.UA

### Сервіс який переглядає оголошення з орендою житла на olx.ua у вибраних населених пунктах та одразу надсилає нові оголошення у необхідну telegram групу

1. Встановити Python3 (https://www.python.org/downloads/), Docker (https://docs.docker.com/engine/install/) та Docker-Compose (https://docs.docker.com/compose/install/).
2. Клонувати проект ```git clone https://github.com/VladimirKritov/hata.git```
3. Створити telegram бота та отримати токен.
   1. Через пошук у telegram знайти бота @BotFather
   
   <img src="readme_images/token_01.jpg" width="240"/>
   
   2. За допомогою команди ```/newbot``` створити нового бота: <ім'я бота>_bot.
   
   <img src="readme_images/token_02.jpg" width="240"/>
   
   3. Зберегти токен після створення бота.
   
   <img src="readme_images/token_03.jpg" width="240"/>
   
4. Створити у telegram групу та додати туди створеного бота. *Обов'язково додати бота в адміністратори групи!*.

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

5. Дізнатися id групи, можна переглянути тут ```https://api.telegram.org/bot<BOT_TOKEN>/getUpdates``` (my_chat_member --> chat --> id)

<img src="readme_images/chat_id.jpg" width="320"/>

6. Створити в корені проекту файл token.txt і там вказати токен бота та id групи:
```commandline
<BOT_TOKEN>
<CHAT_ID>
```
Приклад:
```commandline
5114004139:AAEKliiwO-MPm2PDhb5Ej5wcztBre4TGIUU
-1051663062839
```
7. Створити в корені проекту файл locations.txt і там вказати населені пункти, в яких необхідно здійснювати пошук. Написання населених пунктів необхідно брати з урла на olx.ua, вибираючи там локацію. Наприклад, https://www.olx.ua/d/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/ternopol/?currency=UAH
```commandline
chernovtsy
ternopol
uzhgorod
```
8. Виконати команду запуску у терміналі: ```sh run.sh```
