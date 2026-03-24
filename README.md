# BOT "Good morning" for Telegram

![Screenshot 1](https://user-images.githubusercontent.com/12657938/235433999-d8163841-6a49-49e1-a67c-31f1a71cb5d5.png)
![Screenshot 2](https://user-images.githubusercontent.com/12657938/235433924-9e9af9e4-521d-4e42-bb51-96fc7ff224a4.png)

## Description

Telegram bot that automatically posts greetings, weather, cats, currency and other useful data.

## Current version

- 2.2
- Python 3.10+
- telethon removed
- telebot added
- new modules: `fact`, `wisdom`
- minor fixes

## Installation

```bash
pip3 install -r ./requirements.txt
```

## GPT suggestion

For GPT integration, use `gpt4free`:
https://github.com/xtekky/gpt4free/tree/main

## Configuration (.env)

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

### Required fields

- `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `TELEGRAM_STRING_SESSION`, `TELEGRAM_TOKEN`
- `WEATHER_API_KEY` (OpenWeatherMap)

### Optional fields

- `CAT_URL_404` — fallback cat URL if `cat.py` returns an error
- `GPT_URL` — service URL (e.g. gpt4free)
- `TELEGRAM_GROUP` — `-1234567890` (for posting to a group)
- `TELEGRAM_USER` — username for direct messages
- `HEADER_AUTHORIZATION` — authorization for GPT
- `YANDEX_TOKEN` — Yandex Music API token
- `CAT_API` — api.thecatapi.com key

## How to get Telegram credentials

1. Register an app on Telegram and obtain `API_ID` and `API_HASH`.

## Run

```bash
python3 main.py
```

## Scheduler (cron)

```cron
0 10 * * * /usr/bin/python3 /home/user/main.py >> /var/log/main_bot.log 2>&1
```

## Notes

- `CAT_URL_404` is used as a fallback image if `cat.py` returns an error.
- `GPT_URL` is the address of a ChatGPT or clone service.

## ⚠️ Important

- Do not publish `.env` with real credentials.

## 📄 License

MIT

## 🤝 Contribution

Suggestions are welcome. Open an issue or pull request.