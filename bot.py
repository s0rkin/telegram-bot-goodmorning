#! /usr/bin/env python3

import os
import requests
import json
import datetime
import time

from yaweather import Russia, YaWeather

import urllib.request as url
import xml.etree.ElementTree as et

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

#load file .env config
load_dotenv()

#.env strings - TELEGRAM_STRING_SESSION, TELEGRAM_API_ID, TELEGRAM_API_HASH, WEATHER_API_KEY (for yandex), HEADER (brawser header)
# TELEGRAM_GROUP (id group like -1234567 (int)) or TELEGRAM_USER ("nicname" user like "test").

try:
    client = TelegramClient(StringSession(os.getenv("TELEGRAM_STRING_SESSION")), os.getenv("TELEGRAM_API_ID"), os.getenv("TELEGRAM_API_HASH"))
    client.start()
except Exception as e:
    print(f"Exception while starting the client - {e}")
else:
    print("Client started")

#get weather res.fact.temp and res.fact.feels_like, see api yaweather.
y = YaWeather(api_key=os.getenv("WEATHER_API_KEY"))
#current space for weather
res = y.forecast(Russia.Moscow)
#return full string for telegram "text" + temp
get_temp = "\n\nПогода в Москве: " + str(res.fact.temp) + " °C"
get_temp_feels_like = ", ощущается как " + str(res.fact.feels_like) + " °C"

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
    usd = "\n\nUSD <b>" + (x.find("Value").text) + "</b> руб"
  if id_v == id_euro:
    eur = "\nEURO <b>" + (x.find("Value").text) + "</b> руб"

#function getday for working from work calendar
#get current date/time
today = datetime.datetime.today()

#function getday
def getday():
	try:
		r = requests.get("https://isdayoff.ru/api/getdata?year=" + today.strftime("%Y") + "&month=" + today.strftime("%m") + "&day=" + today.strftime("%d"))
		t = r.text
	except:
		r = getday()
#return full string for telegram "text" + getday()
	if t == '1':
		return 'Доброе утро!☝ Сегодня нерабочий день.'
	elif t == '0' or t == '4':
		return 'Доброе утро!☝ Сегодня рабочий день.'
	elif t == '2':
		return 'Доброе утро!☝ Сегодня сокращённый рабочий день.'
	else:
		return 'Доброе утро!☝ Сегодня ХЗ какой день.'

#function advice of day
def getadvice():
	try:
		r = requests.get("https://fucking-great-advice.ru/api/random")
		t = json.loads(r.text)
	except:
		r = getadvice()
#return full string for telegram "text" + getadvice()
	return "\n\n<b>Совет дня:</b> " + t['text']


#need header for post, doing it
header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest"}

#function generate_random_fact
def generate_random_fact():
	try:
		r = requests.post("https://randstuff.ru/fact/generate/", headers = header)
		t = json.loads(r.text)
	except:
		r = generate_random_fact()
#return full string for telegram "text" + generate_random_fact()
	return "\n<b>Факт дня:</b> " + t["fact"]["text"]

#function getquoute of day
def getquote():
	try:
		r = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=ru")
		t = r.text
	except:
		r = getquote()
#return full string for telegram "text" + getquote()
	return "\n<b>Цитата дня:</b> " + t

#function get file cat
def getcat():
    try:
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
    except:
        url = getcat()
    return url

#main function for send message to telegram chat
async def main():
    try:
        ret_value = await client.send_message(os.getenv("TELEGRAM_USER"), getday() + getadvice() + generate_random_fact() + getquote() + get_temp + get_temp_feels_like + usd + eur, file=getcat(), parse_mode="html")
    except Exception as e:
        print(f"Exception while sending the message - {e}")
    else:
        print(f"Message sent. Return Value {ret_value}")

with client:
    client.loop.run_until_complete(main())
