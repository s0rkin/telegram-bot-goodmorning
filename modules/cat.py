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

#load file .env config
from dotenv import load_dotenv
load_dotenv()

header = {
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST")
    }

param = {
    "api_key": os.getenv("CAT_API"), 
    "mime_types": "jpg,png", 
    "format": "src"
    }

#function get file cat
def get_cat(num_retries = 10):
    error_return = 0
    for attempt_no in range(num_retries):
        try:
            r = requests.get(os.getenv("CAT_URL"), headers = header, params = param)
            url = r.url
            return url
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_cat): " + str(num_retries - 1))
                r = get_cat(num_retries - 1)
            else:
                print("API (get_cat) ERROR! 10 retries expired!")
                error_return = 1
                break
    if error_return == 1:
        return os.getenv("CAT_URL_404")
