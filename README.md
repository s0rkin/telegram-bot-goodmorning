# Бот "Доброе утро" для телеграм, под вашей учеткой!
# BOT "Good morning" for telegram, on your profile.
![Screenshot_1](https://user-images.githubusercontent.com/12657938/177186433-e743280a-ecb7-45f1-b59b-930b94ef9d9e.png)

Устанавливаем библиотеки:
Installing libraries:
`pip3 install -r ./requirements.txt`

TELEGRAM_API_HASH = хэш приложения в телеграм, гуглим как получить.
TELEGRAM_API_HASH = hash app in telegram, google how to catch.

TELEGRAM_API_ID = id приложения в телеграм, гуглим как получить. 
TELGRAM_API_ID = id app in telegram, google how to catch.

get_string_session.py - авторизация в телеге, получаем TELEGRAM_SESSION_STRING и засовываем в env файл.
get_string_session.py - auth in telegram, get TELEGRAM_SESSION_STRING and add to env file.

CAT_API = ключ api https://thecatapi.com/
CAT_API = key api https://thecatapi.com/

WEATHER_API_KEY - ключ апи openweathermap или yandex (закомментил в коде bot.py).
WEATHER_API_KEY - api key for openweathermap or yandex (comment in code bot.py).

TELEGRAM_GROUP - группу в телеграм, формат TELEGRAM_GROUP=-1234567890
TELEGRAM_GROUP - group in telegram, format TELEGRAM_GROUP=-1234567890

How to quickly find out the id of a group or user, go to the web version of telegram, the link will have an identifier of the form - /k/#-123456789, this is the id, it's important! add -100 to the beginning, for example, TELEGRAM_GROUP=-100123456789

TELEGRAM_USER - юзер в телеграм, формат TELEGRAM_USER="user"
TELEGRAM_USER - user in telegram, format TELEGRAM_USER="user"

Функция main в send_message используем либо user,либо group. ну либо комбинации.
The main function in send_message uses either user or group. well, or combinations.

далее запускаем по крону bot.py, например так - 0 10 * * * /usr/bin/python3/home/user/bot.py
next, run on the cron bot.py for example, like this - 0 10 * * * /usr/bin/python3/home/user/bot.py
