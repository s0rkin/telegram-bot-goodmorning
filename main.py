#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.2'
# ---------------------------------------------------------------------------

import os
from datetime import datetime
import json

#import modules
from modules import workday, cat, gpt, valute, yamusic, weather, fact, wisdom
import telebot

#load file .env config
from dotenv import load_dotenv
load_dotenv()

#get current date/time
now = datetime.now()

#text_from text for telegram
text_from = "<code>Сгенерировано нейросетью ChatGPT! by s0rry</code>"

print(now)

# Инициализация бота
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
array_as_string = os.getenv("TELEGRAM_GROUP")

# join groups in array
group_ids = json.loads(array_as_string)

#add values
work_day = workday.get_day()
weather_text = weather.get_weather()
gpt_text = gpt.gpt_fix_text
yamusic_text = yamusic.yaMusic_chart()
valute_text = valute.get_valute()
fact_text = fact.get_random_fact()
wisdom_text = wisdom.get_random_wisdom()
cat_url = cat.get_cat()

# main function
def main():
    # catch music file
    file_path = yamusic.yaMusic_file()

    # check music file path
    if not os.path.exists(file_path):
        print(f"Файл не существует: {file_path}")
        return
    elif os.path.getsize(file_path) == 0:
        print(f"Файл пустой: {file_path}")
        return

    # send msg's for groups
    for group_id in group_ids:
        try:
            #send photo (CAT_URL + text)
            bot.send_photo(
                group_id,
                cat_url,
                caption=work_day + "\n\n" + gpt_text + fact_text + wisdom_text + "\n\n" + weather_text + "\n\n" + yamusic_text + "\n\n" + valute_text + "\n" + text_from,
                parse_mode="html"
            )

            # open music file and send it
            with open(file_path, 'rb') as uploaded:
                bot.send_audio(
                    group_id,
                    uploaded,
                    caption="Трек дня! ☝☝☝"
                )

        except Exception as e:
            print(f"Ошибка при отправке сообщения в группу {group_id}: {e}")
            print("---------------------------------------------------------------------------")
        else:
            print(f"Сообщения успешно отправлены в группу {group_id}")
            print("---------------------------------------------------------------------------")

#start main
if __name__ == "__main__":
    main()