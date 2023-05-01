# Бот "Доброе утро" для телеграм, под вашей учеткой!
# BOT "Good morning" for telegram, on your profile!
![Screenshot_1](https://user-images.githubusercontent.com/12657938/235433999-d8163841-6a49-49e1-a67c-31f1a71cb5d5.png)
![Screenshot_2](https://user-images.githubusercontent.com/12657938/235433924-9e9af9e4-521d-4e42-bb51-96fc7ff224a4.png)

<p>Устанавливаем библиотеки:</p>
<p>Installing libraries:</p>

<code>pip3 install -r ./requirements.txt</code>
</br>
</br>
<p>TELEGRAM_API_HASH = хэш приложения в телеграм, гуглим как получить.</p>
<p>TELEGRAM_API_HASH = hash app in telegram, google how to catch.</p>
</br>
<p>TELEGRAM_API_ID = id приложения в телеграм, гуглим как получить. </p>
<p>TELGRAM_API_ID = id app in telegram, google how to catch.</p>
</br>
<p>get_string_session.py - авторизация в телеге, получаем TELEGRAM_SESSION_STRING и засовываем в env файл.</p>
<p>get_string_session.py - auth in telegram, get TELEGRAM_SESSION_STRING and add to env file.</p>
</br>
<p>CAT_API = ключ api https://thecatapi.com/</p>
<p>CAT_API = key api https://thecatapi.com/</p>
</br>
<p>WEATHER_API_KEY - ключ апи openweathermap или yandex (закомментил в коде bot.py).</p>
<p>WEATHER_API_KEY - api key for openweathermap or yandex (comment in code bot.py).</p>
</br>
<p>TELEGRAM_GROUP - группу в телеграм, формат TELEGRAM_GROUP=-1234567890</p>
<p>TELEGRAM_GROUP - group in telegram, format TELEGRAM_GROUP=-1234567890</p>
</br>
<p>Как быстро узнать id группы или юзера, переходим на web версию телеграм, в ссылке будет идентификатор, вида - /k/#-123456789, это и есть id, важно! добавить в начало -100, например, TELEGRAM_GROUP=-100123456789</p>
<p>How to quickly find out the id of a group or user, go to the web version of telegram, the link will have an identifier of the form - /k/#-123456789, this is the id, it's important! add -100 to the beginning, for example, TELEGRAM_GROUP=-100123456789</p>
</br>
<p>TELEGRAM_USER - юзер в телеграм, формат TELEGRAM_USER="user"</p>
<p>TELEGRAM_USER - user in telegram, format TELEGRAM_USER="user"</p>
</br>
<p>YANDEX_TOKEN = хэш приложения в телеграм, гуглим как получить.</p>
<p>YANDEX_TOKEN = hash app in telegram, google how to catch.</p>
</br>
<p>Функция main в send_message используем либо user,либо group. ну либо комбинации.</p>
<p>The main function in send_message uses either user or group. well, or combinations.</p>
</br>
<p>далее запускаем по крону bot.py, например так - </p>
<p>next, run on the cron bot.py for example, like this - </p>
</br>
  <code>0 10 * * * /usr/bin/python3/home/user/bot.py</code>
