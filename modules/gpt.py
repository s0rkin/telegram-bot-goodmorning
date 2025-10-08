#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.2'
# ---------------------------------------------------------------------------

import os
import requests
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

post_info = {
  "model": "gpt-4", #gpt-4
  "temperature": 0.9, #chaptgpt recomend 0.7-1.0
  "stream": False, 
  "messages": [
    {
        "role": "user", #role's (system, assistant, user)
        "content": "напиши короткий, уникальный совет дня"
    }
  ]
}

#function get_text from chatgpt
def get_text(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.post(os.getenv("GPT_URL"), headers = header, json = post_info)
            t = json.loads(r.text)
            print(t)
            j = t["choices"][0]["message"]["content"]
            #if GPT send in json streaming text...
            if "data:" in j:
                #strings split
                lines = j.strip().split("\n\n")

                #get text
                result = ""
                for line in lines:
                    try:
                        #delete "data: "
                        json_str = line.replace("data: ", "")
                        if not json_str.strip():
                            continue
                        
                        #decode JSON
                        obj = json.loads(json_str)

                        if isinstance(obj, dict) and "content" in obj and obj["content"]:
                            result += obj["content"]
                    except json.JSONDecodeError as e:
                        print(f"Ошибка декодирования JSON: {e}. Строка: {line}")
                        continue
                return "Совет дня:" + result
            else:
                return "Совет дня:" + j
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(60) #wait 60sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_text): " + str(num_retries - attempt_no - 1) + "\n" + str(r.status_code) + "\n" + r.text)
                continue
            else:
                #print for debugging
                print("API (get_text) ERROR! " + str(num_retries) + " retries expired!" + "\n Сервер вернул статус: " + str(r.status_code) + "\n" + r.text)
                return "ChatGPT error! nothing will be send -_-"

#Convert text for telegram
gpt_text = get_text()

if "Совет дня" in gpt_text:
    gpt_text = gpt_text[gpt_text.rfind("Совет дня"):] #remove everything before "Совет дня"

#delete all unwanted symbols
if "*" in gpt_text:
    gpt_text = gpt_text.replace("*", "")
if "#" in gpt_text:
    gpt_text = gpt_text.replace("#", "")
if '"' in gpt_text:
    gpt_text = gpt_text.replace('"', '')

#fix all unwanted spaces and new lines
if "\n\n\n" in gpt_text:
    gpt_text = gpt_text.replace("\n\n\n", "")
if "\n\n" in gpt_text:
    gpt_text = gpt_text.replace("\n\n", "\n")

#fix all unwanted duplicates and wrong words
if "Сегодняшний совет дня:" in gpt_text:
    gpt_text = gpt_text.replace("Сегодняшний совет дня:", "Совет дня:")
if "Сегодняшний совет" in gpt_text:
    gpt_text = gpt_text.replace("Сегодняшний совет", "Совет дня:")

#add bold to "Совет дня:"
if "Совет дня:" in gpt_text:
    gpt_text = gpt_text.replace("Совет дня:", "<b>Совет дня: </b>")
if "Совет дня\n" in gpt_text:
    gpt_text = gpt_text.replace("Совет дня\n", "<b>Совет дня: </b>")
if "</b>\n" in gpt_text:
    gpt_text = gpt_text.replace("</b>\n", "</b>")

#save fixed text for send
gpt_fix_text = gpt_text
print("---DEBUG---")
print(gpt_fix_text)
print("---END DEBUG---")