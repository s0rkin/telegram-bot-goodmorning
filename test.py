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

#function get_text from chatgpt
now = datetime.now()
#check_day = now.strftime("%d день, %m месяц, %Y год.")
check_day = now.strftime("%Y-%m-%d")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    #"X-Requested-With": os.getenv("HEADER_REQUEST"), 
    #"Authorization": os.getenv("HEADER_AUTHORIZATION")
    "Content-Type": "application/json",
    "Authorization": "Bearer " + "pk-this-is-a-real-free-pool-token-for-everyone",
    #"Access Token": "test-1"
    #"Referer": "https://chat1.geekgpt.org/"
    }

post_info = {
    "frequency_penalty": 0,
    "messages": [
        {
            #"content": "Сегодня дата  " + check_day + ". Напиши коротко на эту дату - совет дня, факт дня, цитату дня. Без пожеланий." # + "\n Без ответа на запрос, без самого запроса, без пожеланий"
            #"content": "напиши подробно для bitrix php8 модуль, который подключается к chatgpt и заполняет описание товаров на основании характеристик и наименования товара"
            #"content": "Перепиши описание для товара более развернуто и добавь что знаешь - Люстра Crystal Lux GLORIA SP6 BRASS , Высота, мм	415	,Диаметр, мм	770	,Объем	0.0435	,Вес, кг	8.06	,Бренд	Crystal Lux	,Коллекция	GLORIA	,Страна бренда	Испания	,Стиль	Классика	,Тип цоколя	E14	,Количество ламп	6	,Общая мощность, W	60	,Пульт ДУ	Нет	,Степень защиты	IP20 ,Материал арматуры	Металл	,Материал плафонов	Стекло	,Цвет арматуры	Латунь	,Цвет плафонов	Прозрачный"
            #"content": "напиши продающее СЕО описание световых приборов более развернуто для категории - Шоурум интернет-магазина Benedom.ru ",
            "content": "напиши как посчитать трудозатраты отдела технической поддержки" ,
            "role": "user", #role's (system, assistant, user)
        }
    ],
    "model": "gpt-3.5-turbo",
    "presence_penalty": 0,
    "temperature": 1.0,
    "top_p": 1.0,
    "stream": False
}

def get_text(num_retries = 15):
    for attempt_no in range(num_retries):
        try:
            r = requests.post("http://94.241.138.112:40999/v11234567/v1/chat/completions", headers = header, json = post_info)
            t = json.loads(r.text)
            print(r.text)
            j = t["choices"][0]["message"]["content"]
            return j
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_text): " + str(num_retries))
                r = get_text(num_retries - 1)
            else:
                print("API (get_text) ERROR! " + str(num_retries) + "retries expired!")
                return "ChatGPT error! nothing will be send -_____-" 


gpt_text = get_text()

print(gpt_text)

#Convert text for telegram
#if "Конечно!" in gpt_text:
#    gpt_text = gpt_text.replace("Конечно!", "")
#if "Вот ваш запрос:" in gpt_text:
#    gpt_text = gpt_text.replace("Вот ваш запрос:", "")
#if "Конечно, вот что у меня есть:" in gpt_text:
#    gpt_text = gpt_text.replace("Конечно, вот что у меня есть:", "")
#if "Конечно, вот:" in gpt_text:
#    gpt_text = gpt_text.replace("Конечно, вот:", "")
#if "Конечно, вот ваш запрос:" in gpt_text:
#    gpt_text = gpt_text.replace("Конечно, вот ваш запрос:", "")
#if "Конечно, вот ваше обновление на сегодня:" in gpt_text:
#    gpt_text = gpt_text.replace("Конечно, вот ваше обновление на сегодня:", "")

#if "Совет дня" in gpt_text:
#    gpt_text = gpt_text[gpt_text.rfind("Совет дня"):] #delete all to "Совет дня"
#if "\n\n\n" in gpt_text:
#    gpt_text = gpt_text.replace("\n\n\n", "")
#if "\n\n" in gpt_text:
#    gpt_text = gpt_text.replace("\n\n", "\n")
##if "- Совет" in gpt_text:
##    gpt_text = gpt_text.replace("- Совет", "Совет")
#if "- Факт" in gpt_text:
#    gpt_text = gpt_text.replace("- Факт", "Факт")
#if "- Цитата" in gpt_text:
#    gpt_text = gpt_text.replace("- Цитата", "Цитата")
#if "Совет дня" in gpt_text:
#    gpt_text = gpt_text.replace("Совет дня", "<b>Совет дня")
#if "Факт дня" in gpt_text:
#    gpt_text = gpt_text.replace("Факт дня", "<b>Факт дня")
#if "Цитата дня" in gpt_text:
#    gpt_text = gpt_text.replace("Цитата дня", "<b>Цитата дня")
#if "дня:" in gpt_text:
#    gpt_text = gpt_text.replace("дня:", "дня:</b>")
#if "</b>\n" in gpt_text:
#    gpt_text = gpt_text.replace("</b>\n", "</b>")
#
#print("\n-------------" + "\n" + gpt_text)