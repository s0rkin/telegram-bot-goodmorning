# Бот "Доброе утро" для телеграм, под вашей учеткой!
![Screenshot_1](https://user-images.githubusercontent.com/12657938/177186433-e743280a-ecb7-45f1-b59b-930b94ef9d9e.png)

Устанавливаем библиотеки:
`pip3 install -r ./requirements.txt`

TELEGRAM_API_HASH = хэш приложения в телеграм, гуглим как получить.

TELEGRAM_API_ID = id приложения в телеграм, гуглим как получить. 

get_string_session.py - авторизация в телеге, получаем TELEGRAM_SESSION_STRING и засовываем в env файл.

WEATHER_API_KEY - ключ апи яндекс погоды.

TELEGRAM_GROUP - группу в телеграм, формат TELEGRAM_GROUP=-1234567890

Как быстро узнать id группы или юзера, переходим на web версию телеграм, в ссылке будет идентификатор, вида - /k/#-123456789, это и есть id, важно! добавить в начало -100, например, TELEGRAM_GROUP=-100123456789

TELEGRAM_USER - юзер в телеграм, формат TELEGRAM_USER="user"

Функция main в send_message используем либо user,либо group. ну либо комбинации.

далее запускаем по крону bot.py, например так - 0 10 * * * /usr/bin/python3 /home/user/bot.py
