#! /usr/bin/env python3

import os
import requests
import json
import datetime
import time

#from yaweather import Russia, YaWeather

import urllib.request as url
import xml.etree.ElementTree as et

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

#load file .env config
load_dotenv()

#.env strings - TELEGRAM_STRING_SESSION, TELEGRAM_API_ID, TELEGRAM_API_HASH, WEATHER_API_KEY (for yandex), HEADER (brawser header)
# TELEGRAM_GROUP (id group like -1234567 (int)) or TELEGRAM_USER ("nickname" user like "test").

try:
    client = TelegramClient(StringSession(os.getenv("TELEGRAM_STRING_SESSION")), os.getenv("TELEGRAM_API_ID"), os.getenv("TELEGRAM_API_HASH"))
    client.start()
except Exception as e:
    print(f"Exception while starting the client - {e}")
else:
    print("Client started")

#YANDEX if need

#get weather res.fact.temp and res.fact.feels_like, see api yaweather.
#y = YaWeather(api_key=os.getenv("WEATHER_API_KEY"))
#current space for weather
#res = y.forecast(Russia.Moscow)
#return full string for telegram "text" + temp
#get_temp = "\n\nПогода в Москве: " + str(res.fact.temp) + " °C"
#get_temp_feels_like = ", ощущается как " + str(res.fact.feels_like) + " °C"

#get_weather new from openweathermap 

def get_weather():
    try:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather", params={"id": 524901, "type": "like", "units": "metric", "lang": "ru", "APPID": os.getenv("WEATHER_API_KEY")})
        t = json.loads(r.text)
    except:
        r = get_weather()
    return "\n\nПогода в Москве: " + (str(int(t["main"]["temp"]))) + "°C " + t["weather"][0]["description"] + ", ощущается как " + (str(int(t["main"]["feels_like"])) + "°C")

#USD + EURO
# parse euro + dollar from cbr xml format.
id_dollar = "R01235"
id_euro = "R01239"

web_data = url.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
str_data = web_data.read()
xml_data = et.fromstring(str_data)
quoetes_list = xml_data.findall("Valute")

#get USD and EUR from xml - TODO: function will be better.
for x in quoetes_list:
    id_v = x.get("ID")
    if id_v == id_dollar:
        get_usd = "\n\nUSD <b>" + (x.find("Value").text[:-2]) + "</b> руб"
    if id_v == id_euro:
        get_eur = "\nEURO <b>" + (x.find("Value").text[:-2]) + "</b> руб"

#function get_day for working from work calendar
#get current date/time
today = datetime.datetime.today()

#function get_day
def get_day():
    try:
        r = requests.get("https://isdayoff.ru/api/getdata", params={"year": today.strftime("%Y"), "month": today.strftime("%m"), "day": today.strftime("%d")})
        t = r.text
    except:
        r = get_day()
#return full string for telegram "text" + get_day()
    if t == "1":
        return "Доброе утро!☝ Сегодня нерабочий день."
    elif t == "0" or t == "4":
        return "Доброе утро!☝ Сегодня рабочий день."
    elif t == "2":
        return "Доброе утро!☝ Сегодня сокращённый рабочий день."
    else:
        return "Доброе утро!☝ Сегодня ХЗ какой день."

#function get_advice of day
def get_advice():
    try:
        r = requests.get("https://fucking-great-advice.ru/api/random")
        t = json.loads(r.text)
    except:
        r = get_advice()
#return full string for telegram "text" + get_advice()
    return "\n\n<b>Совет дня:</b> " + t["text"]

#need header for post, doing it
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}

#function get_random_fact
def get_random_fact():
    try:
        r = requests.post("https://randstuff.ru/fact/generate/", headers = header)
        t = json.loads(r.text)
    except:
        r = get_random_fact()
#return full string for telegram "text" + get_random_fact()
    return "\n<b>Факт дня:</b> " + t["fact"]["text"]

#function get_quote of day
def get_quote():
    try:
        r = requests.get("https://api.forismatic.com/api/1.0/", params={"method": "getQuote", "format": "text", "lang": "ru"})
        t = r.text
    except:
        r = get_quote()
#return full string for telegram "text" + get_quote()
    return "\n<b>Цитата дня:</b> " + t

#function get file cat
def get_cat():
    try:
        r = requests.get("https://api.thecatapi.com/api/images/get", params={"api_key": os.getenv("CAT_API"), "mime_types": "jpg,png", "format": "src"})
        url = r.url
    except:
        url = get_cat()
    return url

#main function for send message to telegram chat
async def main():
    try:
        ret_value = await client.send_message(os.getenv("TELEGRAM_USER"), get_day() + get_advice() + get_random_fact() + get_quote() + get_weather() + get_usd + get_eur, file=get_cat(), parse_mode="html")
    except Exception as e:
        print(f"Exception while sending the message - {e}")
    else:
        print(f"Message sent. Return Value {ret_value}")

with client:
    client.loop.run_until_complete(main())
