#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.2
# ---------------------------------------------------------------------------

import os
import time
import urllib.request as url
import xml.etree.ElementTree as et

#load file .env config
from dotenv import load_dotenv
load_dotenv()

#USD + EURO
# parse euro + dollar from cbr xml format.
usd_id = os.getenv("USD_ID")
euro_id = os.getenv("EURO_ID")
cny_id = os.getenv("CNY_ID")

def get_valute(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            web_data = url.urlopen(os.getenv("VALUTE_URL"))
            str_data = web_data.read()
            xml_data = et.fromstring(str_data)
            quoetes_list = xml_data.findall("Valute")

            #get USD and EUR from xml
            for x in quoetes_list:
                id_v = x.get("ID")
                if id_v == usd_id:
                    get_usd = "USD <b>" + (x.find("Value").text[:-2]) + "</b> руб"
                if id_v == euro_id:
                    get_eur = "\nEURO <b>" + (x.find("Value").text[:-2]) + "</b> руб"
                if id_v == cny_id:
                    get_cny = "\nCNY <b>" + (x.find("Value").text[:-2]) + "</b> руб"
                    
            return get_usd + get_eur + get_cny
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_valute): " + str(num_retries - attempt_no - 1))
                continue
            else:
                print("API (get_valute) ERROR! " + str(num_retries) + " retries expired!")
                return "USD: error 0 руб." + "\nUERO: error 0 руб." + "\nCNY: error 0 руб."