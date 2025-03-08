#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.2'
# ---------------------------------------------------------------------------

import requests
import os
import json 
import time

#load file .env config
from dotenv import load_dotenv
load_dotenv()

header = {
    "Accept": "application/json; charset=utf-8",
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST"), 
    }

def get_random_fact(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.post(os.getenv("FACT_URL"), headers = header)
            t = json.loads(r.text)
            return "\n<b>Факт дня:</b> " + t["fact"]["text"]
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_random_fact): " + str(num_retries - attempt_no - 1))
                continue
            else:
                print("API (get_random_fact) ERROR! 10 retries expired!")
                return "\n<b>Факт дня:</b> API ERROR! 10 retries expired!"