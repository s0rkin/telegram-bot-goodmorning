# BOT "Good morning" for telegram, on your profile!
![image](https://github.com/s0rkin/telegram-bot-goodmorning/assets/12657938/23614b81-c836-4877-b38f-b19ff99c7e0a)
![image](https://github.com/s0rkin/telegram-bot-goodmorning/assets/12657938/1109df36-0aef-4882-b157-9c290a7d9d23)


<p>Current ver. 2.1
<code>
*add GPT
*refactoring
*add mass config's
*add modules
*fix's
</code>
</p>
<p>Installing libraries:
<code>pip3 install -r ./requirements.txt</code>
</p>
<p>
FOR YAMUSIC need python3.7!!! its very important!
</p>
<br>
<p>CONFIG in <code>.env</code>:
<code>
  PATH_FOR_MUSIC="/home/user/" 
  MUSIC_EXCEPT=
  TELEGRAM_API_ID=
  TELEGRAM_API_
  TELEGRAM_STRING_SESSION=
  WEATHER_API_KEY=
  CAT_URL="https://api.thecatapi.com/api/images/get"
  CAT_URL_404=
  CAT_API=
  CALENDAR_URL="https://api.sm.su/v1/calendar/business/"
  WEATHER_URL="https://api.openweathermap.org/data/2.5/weather"
  VALUTE_URL="http://www.cbr.ru/scripts/XML_daily.asp"
  GPT_URL=
  USD_ID="R01235"
  EURO_ID="R01239"
  CNY_ID="R01375"
  TELEGRAM_GROUP=
  TELEGRAM_USER=
  YANDEX_TOKEN=
  HEADER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0  Safari/537.36"
  HEADER_REQUEST="XMLHttpRequest"
  HEADER_AUTHORIZATION=
</code>
</p>
<p>
u need to add some base URL -
</p>
<p>
MUSIC_EXCEPT - need add something music file name if yamusic.py got except.
</p>
<p>
CAT_URL_404 - that url send default img from <code>cat.py</code> if error.
</p>
<p>
GPT_URL - chatgpt url , google it! can be free! =)</text>
</p>
<p>then u need add - 
</p>
<p>
TELEGRAM_GROUP - EXAMPLE -> TELEGRAM_GROUP=-1234567890  // see more on <code>main.py</code> client send message!
</p>
<p>
TELEGRAM_USER - if need, EXAMPLE -> TELEGRAM_USER="user"
</p>
<p>
HEADER_AUTHORIZATION - this is authorization for GPT! - see more in <code>gpt.py</code> (u need add url and header's). google it!
</p>
<p>then u need add -</p>
<p>
WEATHER_API_KEY - key for openweathermap its free, google it.
</p>
<p>
YANDEX_TOKEN - google it. TOKEN for yandex music app.
</p>
<p>
CAT_API_KEY - key for api.thecatapi.com its free, google it.
</p>
<p>
add TELEGRAM config's google how to catch. or use <code>get_string_session.py</code>
</p>
<p>
TELEGRAM_API_ID=
</p>
<p>
TELEGRAM_API_HASH=
</p>
<p>
TELEGRAM_STRING_SESSION=
</p>
<p>ADD TO CRON, EXAMPLE:
<code>0 10 * * * /usr/bin/python3.7 /home/user/main.py >> /var/log/main_bot.log</code>
</p>
