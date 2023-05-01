#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.0'
# ---------------------------------------------------------------------------
import os
import requests
import json
import datetime
import time
import random

from yandex_music import Client as yaClient

#from yaweather import Russia, YaWeather

import urllib.request as url
import xml.etree.ElementTree as et

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

#load file .env config
load_dotenv()

#need header for post requests, doing it
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}

#get current date/time
today = datetime.datetime.today()

#.env strings - TELEGRAM_STRING_SESSION, TELEGRAM_API_ID, TELEGRAM_API_HASH, WEATHER_API_KEY (for yandex), YANDEX_TOKEN (for yandex music google it)
# TELEGRAM_GROUP (id group like -1234567 (int)) or TELEGRAM_USER ("nickname" user like "test").
print("---------------------------------------------------------------------------")
print(today)

#YANDEX MUSIC chart + file
CHART_ID = 'world'

def yaMusic_chart(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            yclient = yaClient(os.getenv("YANDEX_TOKEN")).init()
            chart = yclient.chart(CHART_ID).chart

            text = [f'🏆 ТОП-5 треков Ямузыки:']
            for track_short in chart.tracks[:5]:
                track, chart = track_short.track, track_short.chart
                artists = ''
                if track.artists:
                    artists = ', '.join(artist.name for artist in track.artists) + ' - '

                track_text = f'{artists}{track.title}'

                if chart.progress == 'down':
                    track_text = '🔻 ' + track_text
                elif chart.progress == 'up':
                    track_text = '🔺 ' + track_text
                elif chart.progress == 'new':
                    track_text = '🆕 ' + track_text
                elif chart.position == 1:
                    track_text = '👑 ' + track_text

                track_text = f'{chart.position}. {track_text}'
                text.append(track_text)
            chartTrack = ('\n'.join(text))
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                yclient = yaMusic_chart(num_retries - 1)
                print("CURRENT RETRY (yaMusic_chart): " + num_retries)
            else:
                print("API (yaMusic_chart) ERROR! 10 retries expired!")
                raise
                #TODO: need return text if api error or something got error. sothing like this: Yandex API error: unavailable chart.
        return chartTrack

def yaMusic_file(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            yclient = yaClient(os.getenv("YANDEX_TOKEN")).init()

            music = yclient.users_likes_tracks()[0].fetch_track()
            getTrack = yclient.rotor_station_tracks(station='user:onyourwave')
            getTrackInfo = getTrack["sequence"][random.randint(0,4)] #random track from onyourwave. (onyourwave send only 5 tracks, random it 1-5)
            getTrackId = getTrackInfo["track"]["id"]
            musicFile = yclient.tracks_download_info(track_id=getTrackId)[0].download("/home/user/music/" + str.capitalize(getTrackInfo["track"]["artists"][0]["name"]) + " - " + str.capitalize(getTrackInfo["track"]["title"]) + '.mp3')
            musicFilePath = "/home/user/music/" + str.capitalize(getTrackInfo["track"]["artists"][0]["name"]) + " - " + str.capitalize(getTrackInfo["track"]["title"]) + '.mp3'
            print("Путь до файла с музякой: " + musicFilePath)
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                yclient = yaMusic_file(num_retries - 1)
                print("CURRENT RETRY (yaMusic_file): " + num_retries)
            else:
                print("API (yaMusic_file) ERROR! 10 retries expired!")
                raise
                #TODO: need return random mp3 file from /home/user + text if api error or something got error.
        return musicFilePath

#END YANDEX MUSIC

try:
    client = TelegramClient(StringSession(os.getenv("TELEGRAM_STRING_SESSION")), os.getenv("TELEGRAM_API_ID"), os.getenv("TELEGRAM_API_HASH"))
    client.start()
except Exception as e:
    print(f"Exception while starting the client - {e}")
else:
    print("Client started")

#YANDEX WEATHER if need

#get weather res.fact.temp and res.fact.feels_like, see api yaweather.
#y = YaWeather(api_key=os.getenv("WEATHER_API_KEY"))
#current space for weather
#res = y.forecast(Russia.Moscow)
#return full string for telegram "text" + temp
#get_temp = "\n\nПогода в Москве: " + str(res.fact.temp) + " °C"
#get_temp_feels_like = ", ощущается как " + str(res.fact.feels_like) + " °C"

#get_weather new from openweathermap 

def get_weather(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.get("https://api.openweathermap.org/data/2.5/weather", headers = header, params={"id": 524901, "type": "like", "units": "metric", "lang": "ru", "APPID": os.getenv("WEATHER_API_KEY")})
            t = json.loads(r.text)
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                r = get_weather(num_retries - 1)
                print("CURRENT RETRY (get_weather): " + num_retries)
            else:
                print("API (get_weather) ERROR! 10 retries expired!")
                return "\n\nПогода в Москве: не удалось получить, API ERROR! 10 retries expired!"
        return "\n\nПогода в Москве: " + (str(int(t["main"]["temp"]))) + "°C " + t["weather"][0]["description"] + ", ощущается как " + (str(int(t["main"]["feels_like"])) + "°C")

#USD + EURO
# parse euro + dollar from cbr xml format.
#TODO: function with except and text errors. refactoring and etc.
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
def get_day(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.get("https://api.sm.su/v1/calendar/business/", headers = header, params={"day": today.strftime("%Y-%m-%d")})
            t = json.loads(r.text)
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                r = get_day(num_retries - 1)
                print("CURRENT RETRY (get_day): " + num_retries)
            else:
                print("API (get_day) ERROR! 10 retries expired!")
                return "Доброе утро!☝ Сегодня ХЗ какой день. get_day API ERROR! 10 retries expired!"
        #return full string for telegram "text" + get_day()
        if t["work"] == "1":
            return "Доброе утро!☝ Сегодня " + t["type"] + "."
        elif t["work"] == "0" and (t["zag"] == "Календарный выходной день" or t["zag"] == "Перенесенный день"):
            return "Доброе утро!☝ Сегодня " + t["type"] + "."
        elif t["work"] == "0":
            return "Доброе утро!☝ Сегодня " + t["type"] + ". " + t["zag"] + "."
        else:
            return "Доброе утро!☝ Сегодня ХЗ какой день."

#function get_advice of day
def get_advice(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.get("https://fucking-great-advice.ru/api/random", headers = header)
            t = json.loads(r.text)
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                r = get_advice(num_retries - 1)
                print("CURRENT RETRY (get_advice): " + num_retries)
            else:
                print("API (get_advice) ERROR! 10 retries expired!")
                return "Совет дня: get_advice API ERROR! 10 retries expired!"
        #return full string for telegram "text" + get_advice()
        return "\n\n<b>Совет дня:</b> " + t["text"]

#function get_random_fact
def get_random_fact(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.post("https://randstuff.ru/fact/generate/", headers = header)
            t = json.loads(r.text)
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                r = get_random_fact(num_retries - 1)
                print("CURRENT RETRY (get_random_fact): " + num_retries)
            else:
                print("API (get_random_fact) ERROR! 10 retries expired!")
                return "\n<b>Факт дня:</b> get_random_fact API ERROR! 10 retries expired!"
    #return full string for telegram "text" + get_random_fact()
        return "\n<b>Факт дня:</b> " + t["fact"]["text"]

#function get_quote of day
def get_quote(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.get("https://api.forismatic.com/api/1.0/", headers = header, params={"method": "getQuote", "format": "text", "lang": "ru"})
            t = r.text
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                r = get_quote(num_retries - 1)
                print("CURRENT RETRY (get_quote): " + num_retries)
            else:
                print("API (get_quote) ERROR! 10 retries expired!")
                return "\n<b>Цитата дня:</b> get_quote API ERROR! 10 retries expired!"
        #return full string for telegram "text" + get_quote()
        return "\n<b>Цитата дня:</b> " + t

#function get file cat
def get_cat(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.get("https://api.thecatapi.com/api/images/get", headers = header, params={"api_key": os.getenv("CAT_API"), "mime_types": "jpg,png", "format": "src"})
            url = r.url
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                r = get_cat(num_retries - 1)
                print("CURRENT RETRY (get_cat): " + num_retries)
            else:
                print("API (get_cat) ERROR! 10 retries expired!")
                return "https://test.ru/404.jpg" #need 404 url foto
        return url

#main function for send message to telegram chat
async def main():
    try:
        uploaded = await client.upload_file(yaMusic_file())
        ret_value = await client.send_message(os.getenv("TELEGRAM_USER"), get_day() + get_advice() + get_random_fact() + get_quote() + get_weather() + "\n\n" + yaMusic_chart() + get_usd + get_eur, file=get_cat(), parse_mode="html")
        ret_value = await client.send_message(os.getenv("TELEGRAM_USER"), "Трек дня! ☝☝☝", file=uploaded, parse_mode="html")
    except Exception as e:
        print(f"Exception while sending the message - {e}")
    else:
        print(f"Message sent. Return Value {ret_value}")

with client:
    client.loop.run_until_complete(main())
