# BOT "Good morning" for Telegram (на ваш профиль)

![Screenshot 1](https://user-images.githubusercontent.com/12657938/235433999-d8163841-6a49-49e1-a67c-31f1a71cb5d5.png)
![Screenshot 2](https://user-images.githubusercontent.com/12657938/235433924-9e9af9e4-521d-4e42-bb51-96fc7ff224a4.png)

## Описание

Телеграм-бот, который автоматически публикует приветствия, погоду, котиков, валюту и другие полезные данные.

## Текущая версия

- 2.2
- Python 3.10+
- telethon удалён
- telebot добавлен
- новые модули: `fact`, `wisdom`
- мелкие исправления

## Установка

```bash
pip3 install -r ./requirements.txt
```

## Рекомендация по GPT

Для интеграции GPT можно использовать `gpt4free`:
https://github.com/xtekky/gpt4free/tree/main

## Конфигурация (.env)

```dotenv
PATH_FOR_MUSIC="/home/user/"
TELEGRAM_API_ID=
TELEGRAM_API_HASH=
TELEGRAM_STRING_SESSION=
TELEGRAM_TOKEN=
WEATHER_API_KEY=
CAT_URL="https://api.thecatapi.com/v1/images/search"
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
HEADER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
HEADER_REQUEST="XMLHttpRequest"
HEADER_AUTHORIZATION=
```

### Обязательные поля

- `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `TELEGRAM_STRING_SESSION`, `TELEGRAM_TOKEN`
- `WEATHER_API_KEY` (OpenWeatherMap)

### Опции

- `CAT_URL_404` — URL резервного котика, если `cat.py` возвращает ошибку
- `GPT_URL` — URL сервиса (например, gpt4free)
- `TELEGRAM_GROUP` — `-1234567890` (для отправки в группу)
- `TELEGRAM_USER` — имя пользователя для личных сообщений
- `HEADER_AUTHORIZATION` — авторизация для GPT
- `YANDEX_TOKEN` — токен Yandex Music API
- `CAT_API` — ключ api.thecatapi.com

## Как получить данные Telegram

1. Зарегистрировать приложение в Telegram и получить `API_ID` и `API_HASH`.
2. Сформировать `STRING_SESSION` через `get_string_session.py`.

## Запуск

```bash
python3 main.py
```

## Поставить в cron

```cron
0 10 * * * /usr/bin/python3 /home/user/main.py >> /var/log/main_bot.log 2>&1
```

## Полезные заметки

- `CAT_URL_404` нужен для подстановки дефолтной картинки, если `cat.py` возвращает ошибку.
- `GPT_URL` — адрес ChatGPT/клон-сервиса.
- Запр_ещено публиковать `.env` с реальными данными.

## Лицензия

MIT

