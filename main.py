#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.1'
# ---------------------------------------------------------------------------
import os
from datetime import datetime

#import modules
from modules import calendar, cat, gpt, valute, yamusic, weather

#import telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

#load file .env config
from dotenv import load_dotenv
load_dotenv()

#TODO: \n\n need on send message only! not for def's!!!
#TODO: see yamusic.py for refactoring
#TODO: need fix - int(os.getenv) - when group. Exception while sending the message - Cannot find any entity corresponding to "-1001312137891"
#TODO: music?
#TODO: mb new def need.

#get current date/time
now = datetime.now()

#text_from text for telegram
text_from = '<code>Сгенерировано нейросетью ChatGPT4! by s0rry</code>'

print("---------------------------------------------------------------------------")
print(now)

print("START TESTS!")
print("test for get_cat: " + cat.get_cat())
print("---------------------------------------------------------------------------")
print("test for get_day: " + calendar.get_day())
print("---------------------------------------------------------------------------")
print("test for get_text: " + gpt.gpt_text)
print("---------------------------------------------------------------------------")
print("test for get_weather: " + weather.get_weather())
print("---------------------------------------------------------------------------")
print("test for get_valute: " + valute.get_valute())

print("END TESTS!")
print("---------------------------------------------------------------------------")

#TELEGRAM: Start client.
try:
    client = TelegramClient(StringSession(os.getenv("TELEGRAM_STRING_SESSION")), os.getenv("TELEGRAM_API_ID"), os.getenv("TELEGRAM_API_HASH"))
    client.start()
except Exception as e:
    print(f"Exception while starting the client - {e}")
else:
    print("Client started")

#main function for send message to telegram chat
async def main():
    try:
        uploaded = await client.upload_file(yamusic.yaMusic_file())
        #client.send_message need int for group only!
        #(os.getenv("TELEGRAM_USER") // (int(os.getenv("TELEGRAM_GROUP"))
        ret_value = await client.send_message(int(os.getenv("TELEGRAM_GROUP")), calendar.get_day() + "\n\n" + gpt.gpt_text + "\n\n" + weather.get_weather() + "\n\n" + yamusic.yaMusic_chart() + "\n\n" + valute.get_valute()+ "\n" + text_from, file=cat.get_cat(), parse_mode="html")
        ret_value = await client.send_message(int(os.getenv("TELEGRAM_GROUP")), "Трек дня! ☝☝☝", file=uploaded, parse_mode="html")
    except Exception as e:
        print(f"Exception while sending the message - {e}")
    else:
        print(f"Message sent. Return Value {ret_value}")

#end and close when main() complete.
with client:
    client.loop.run_until_complete(main())