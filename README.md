# Бот "Доброе утро" для телеграм, под вашей учеткой!
![Screenshot_1](https://user-images.githubusercontent.com/12657938/177186433-e743280a-ecb7-45f1-b59b-930b94ef9d9e.png)

Устанавливаем библиотеки - pip3 install yaweather && pip3 install python-dotenv && pip3 install telethon

TELEGRAM_API_HASH = хэш приложения в телеграм, гуглим как получить.

TELEGRAM_API_ID = id приложения в телеграм, гуглим как получить. 

WEATHER_API_KEY - ключ апи яндекс погоды.

TELEGRAM_GROUP - группу в телеграм, формат TELEGRAM_GROUP=-1234567890

TELEGRAM_USER - юзер в телеграм, формат TELEGRAM_USER="user"

в send_message используем либо user,либо group. ну либо комбинации.

get_string_session.py - авторизация в телеге, получаем все данные и засовываем в env файл.

далее запускаем по крону bot.py, например так - 0 10 * * * /usr/bin/python3 /home/user/bot.py
