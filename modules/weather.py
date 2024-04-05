#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.1'
# ---------------------------------------------------------------------------

import os
import requests
import time
import json

#load file .env config
from dotenv import load_dotenv
load_dotenv()

header = {
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST")
    }

param = {
    "id": 524901,
    "type": "like", 
    "units": "metric", 
    "lang": "ru", 
    "APPID": os.getenv("WEATHER_API_KEY")
    }

def get_weather(num_retries = 10):
    error_return = 0
    if error_return == 0:
        for attempt_no in range(num_retries):
            try:
                r = requests.get(os.getenv("WEATHER_URL"), headers = header, params = param)
                t = json.loads(r.text)

                return "<b>Погода в Москве:</b> " + (str(int(t["main"]["temp"]))) + "°C " + t["weather"][0]["description"] + ", ощущается как " + (str(int(t["main"]["feels_like"])) + "°C")
            except:
                if attempt_no < (num_retries - 1):
                    time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                    print("CURRENT RETRY (get_weather): " + str(num_retries - 1))
                    r = get_weather(num_retries - 1)
                else:
                    print("API (get_weather) ERROR! 10 retries expired!")
                    error_return += 1
                    break
    else:
        return "<b>Погода в Москве:</b> не удалось получить, API ERROR! " + str(num_retries) + " retry expired!"