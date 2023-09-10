# BOT "Good morning" for telegram, on your profile!
![Screenshot_1](https://user-images.githubusercontent.com/12657938/235433999-d8163841-6a49-49e1-a67c-31f1a71cb5d5.png)
![Screenshot_2](https://user-images.githubusercontent.com/12657938/235433924-9e9af9e4-521d-4e42-bb51-96fc7ff224a4.png)

<p>Current ver. 2.1 </p>
<code>*add GPT
  *refactoring
  *add mass config's
  *add modules
  *fix's
</code>

<p>Installing libraries:</p>
<code>pip3 install -r ./requirements.txt</code>
</br>
</br>
<p>TELEGRAM_API_HASH = hash app in telegram, google how to catch.</p>
</br>
<p>TELGRAM_API_ID = id app in telegram, google how to catch.</p>
</br>
<p>get_string_session.py - авторизация в телеге, получаем TELEGRAM_SESSION_STRING и засовываем в env файл.</p>
<p>get_string_session.py - auth in telegram, get TELEGRAM_SESSION_STRING and add to env file.</p>
</br>
<p>CAT_API = key api https://thecatapi.com/</p>
</br>
<p>WEATHER_API_KEY - api key for openweathermap or yandex (comment in code bot.py).</p>
</br>
<p>TELEGRAM_GROUP - group in telegram, format TELEGRAM_GROUP=-1234567890</p>
</br>
<p>How to quickly find out the id of a group or user, go to the web version of telegram, the link will have an identifier of the form - /k/#-123456789, this is the id, it's important! add -100 to the beginning, for example, TELEGRAM_GROUP=-100123456789</p>
</br>
<p>TELEGRAM_USER - user in telegram, format TELEGRAM_USER="user"</p>
</br>
<p>YANDEX_TOKEN = hash yandex music, google how to catch.</p>
</br>
<p>The main function in send_message uses either user or group. well, or combinations.</p>
</br>
<p>next, run on the cron bot.py for example, like this with loging - </p>
</br>
  <code>0 10 * * * /usr/bin/python3 /home/user/bot.py >> /var/log/bot.log</code>
