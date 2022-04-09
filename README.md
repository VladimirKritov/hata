
# hata - пошук житла на OLX.UA

1. Встановити Python3 (https://www.python.org/downloads/), Docker (https://docs.docker.com/engine/install/) та Docker-Compose (https://docs.docker.com/compose/install/).
2. Клонувати проект ```git clone https://github.com/VladimirKritov/hata.git```
3. Створити telegram бота та отримати токен.
   1. Через пошук у telegram знайти бота @BotFather
   2. За допомогою команди ```/newbot``` створити нового бота: <ім'я бота>_bot.
   3. Зберегти токен після створення бота.
4. Створити у telegram групу та додати туди створеного бота. *Обов'язково додати бота в адміністратори групи!*.
5. Дізнатися id групи, можна переглянути тут ```https://api.telegram.org/bot<BOT_TOKEN>/getUpdates``` (my_chat_member --> chat --> id)
6. Створити в корені проекту файл token.txt і там вказати токен бота та id групи:
```commandline
<BOT_TOKEN>
<CHANNEL_ID>
```
6. Створити в корені проекту файл locations.txt і там вказати населені пункти, в яких необхідно здійснювати пошук. Написання населених пунктів необхідно брати з урла на olx.ua, вибираючи там локацію. Наприклад, https://www.olx.ua/d/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/ternopol/?currency=UAH
```commandline
chernovtsy
ternopol
uzhgorod
```
7. Виконати команду запуску у терміналі: ```sh run.sh```
