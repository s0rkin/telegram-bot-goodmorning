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

now = datetime.now()
#check_day = now.strftime("%d день, %m месяц, %Y год.")
check_day = now.strftime("%m месяц, %d день")

header = {
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST"), 
    "Authorization": os.getenv("HEADER_AUTHORIZATION")
    }

post_info = {
  "messages": [
    {
        "role": "user", #role's (system, assistant, user)
        "content": "Сегодня " + check_day + ". Напиши коротко на сегодня - совет дня, факт дня, цитату дня. Без пожеланий."
    }
  ],
  "model": 'gpt-4o-mini', #gpt-4
  "temperature": 1, #chaptgpt recomend 0.7-1.0
  "presence_penalty": 0,
  "top_p": 1, #chaptgpt recomend 0.7-1.0
  "frequency_penalty": 0,
  "stream": False
}

#function get_text from chatgpt
def get_text(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.post(os.getenv("GPT_URL"), headers = header, json = post_info)
            print(r.text)
            t = json.loads(r.text)
            j = t["choices"][0]["message"]["content"]
            #if GPT send stream: False
            if "data:" in j:
                lines = j.strip().split("\n\n")
                result = ""
                for line in lines:
                    try:
                        json_str = line.replace("data: ", "")
                        
                        if not json_str.strip():
                            continue

                        obj = json.loads(json_str)

                        if isinstance(obj, dict) and "content" in obj and obj["content"]:
                            result += obj["content"]
                    except json.JSONDecodeError as e:
                        print(f"Ошибка декодирования JSON: {e}. Строка: {line}")
                        continue
                return result
            else:
                return j
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(60) #wait 60sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_text): " + str(num_retries - attempt_no - 1) + "\n" + str(r.status_code) + "\n" + r.text)
                continue
            else:
                #print for debugging
                print("API (get_text) ERROR! " + str(num_retries) + " retries expired!" + "\n Сервер вернул статус: " + str(r.status_code) + "\n" + r.text)
                return "ChatGPT error! nothing will be send -_-"

gpt_text = get_text()

#Convert text for telegram
if "Совет дня" in gpt_text:
    gpt_text = gpt_text[gpt_text.rfind("Совет дня"):] #remove everything before "Совет дня"
if "\n\n\n" in gpt_text:
    gpt_text = gpt_text.replace("\n\n\n", "")
if "\n\n" in gpt_text:
    gpt_text = gpt_text.replace("\n\n", "\n")
if "- Факт" in gpt_text:
    gpt_text = gpt_text.replace("- Факт", "Факт")
if "- Цитата" in gpt_text:
    gpt_text = gpt_text.replace("- Цитата", "Цитата")
if " Факт" in gpt_text:
    gpt_text = gpt_text.replace(" Факт", "Факт")
if "Сегодняшний факт дня:" in gpt_text:
    gpt_text = gpt_text.replace("Сегодняшний факт дня:", "")
if " Цитата" in gpt_text:
    gpt_text = gpt_text.replace(" Цитата", "Цитата")
if "Совет дня" in gpt_text:
    gpt_text = gpt_text.replace("Совет дня", "<b>Совет дня")
if "Факт дня" in gpt_text:
    gpt_text = gpt_text.replace("Факт дня", "<b>Факт дня")
if "Цитата дня" in gpt_text:
    gpt_text = gpt_text.replace("Цитата дня", "<b>Цитата дня")
if "дня:" in gpt_text:
    gpt_text = gpt_text.replace("дня:", "дня: </b>")
if "Факт дня: Факт дня:" in gpt_text:
    gpt_text = gpt_text.replace("Факт дня: Факт дня:", "Факт дня:")
if "*" in gpt_text:
    gpt_text = gpt_text.replace("*", "")
if "#" in gpt_text:
    gpt_text = gpt_text.replace("#", "")
if "</b>\n" in gpt_text:
    gpt_text = gpt_text.replace("</b>\n", "</b>")
