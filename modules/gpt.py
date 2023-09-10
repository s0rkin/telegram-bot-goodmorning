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
import json
import time
from datetime import datetime

#load file .env config
from dotenv import load_dotenv
load_dotenv()

#function get_text from chatgpt
now = datetime.now()
check_day = now.strftime("%d.%m")

header = {
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST"), 
    "Authorization": os.getenv("HEADER_AUTHORIZATION")
    }

post_info = {
  "messages": [
    {
      "role": "user",
      "content": "Напиши короткий совет дня, короткий факт дня на " + check_day + " дату, короткую цитату дня "
    }
  ],
  "model": "gpt-4",
  "temperature": 1,
  "presence_penalty": 0,
  "top_p": 1,
  "frequency_penalty": 0,
  "stream": False
}

def get_text(num_retries = 15):
    for attempt_no in range(num_retries):
        try:
            r = requests.post(os.getenv("GPT_URL"), headers=header, json=post_info)
            t = json.loads(r.text)
            j = t["choices"][0]["message"]["content"]
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(60) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_text): " + str(num_retries - 1))
                r = get_text(num_retries - 1)
            else:
                print("API (get_text) ERROR! " + str(num_retries) + "retries expired!")
                return "ChatGPT error! nothing will be send -_____-" 
        return j

gpt_text = get_text()

#Convert text for telegram
if "Конечно!" in gpt_text:
    gpt_text = gpt_text.replace("Конечно!", "")
if "\n\n\n" in gpt_text:
    gpt_text = gpt_text.replace("\n\n\n", "\n")
if "Факт дня" in gpt_text:
    gpt_text = gpt_text.replace("Факт дня", "<b>Факт дня")
if "Совет дня" in gpt_text:
    gpt_text = gpt_text.replace("Совет дня", "<b>Совет дня")
if "Цитата дня" in gpt_text:
    gpt_text = gpt_text.replace("Цитата дня", "<b>Цитата дня")
if ":" in gpt_text:
    gpt_text = gpt_text.replace(":", ":</b>")