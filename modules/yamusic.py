#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.2'
# ---------------------------------------------------------------------------

import os
import time
import random
from yandex_music import Client as yaClient

#load file .env config
from dotenv import load_dotenv
load_dotenv()

#YANDEX MUSIC chart + file
CHART_ID = 'world'
file_path = os.getenv("PATH_FOR_MUSIC")

def yaMusic_chart(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            yclient = yaClient(os.getenv("YANDEX_TOKEN")).init()
            chart = yclient.chart(CHART_ID).chart
            text = [f'🏆 ТОП-5 треков Ямузыки:']
            for track_short in chart.tracks[:5]:
                track, chart = track_short.track, track_short.chart
                artists = ''
                if track.artists:
                    artists = ', '.join(artist.name for artist in track.artists) + ' - '
                track_text = f'{artists}{track.title}'

                if chart.progress == 'down':
                    track_text = '🔻 ' + track_text
                elif chart.progress == 'up':
                    track_text = '🔺 ' + track_text
                elif chart.progress == 'new':
                    track_text = '🆕 ' + track_text
                elif chart.position == 1:
                    track_text = '👑 ' + track_text

                track_text = f'{chart.position}. {track_text}'
                text.append(track_text)

            chartTrack = ('\n'.join(text))

            return chartTrack
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (yaMusic_chart): " + str(num_retries - attempt_no - 1))
                continue
            else:
                print("Yandex API error: unavailable chart! " + str(num_retries) + " retries expired!")
                return "Yandex API error: unavailable chart!"

def yaMusic_file(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            yclient = yaClient(os.getenv("YANDEX_TOKEN")).init()

            #SETING'S for onyourwave yamusic! 
            #available setting's for mood_energy: fun, active, calm, sad, all.
            #available setting's for diversity: favorite, popular, discover, default.
            #available setting's for language: not-russian, russian, any.
            random_mood = ["fun", "active", "calm", "sad", "all"]
            random_diversity = ["favorite", "popular", "discover", "default"]
            random_lang = ["not-russian","russian", "any"]

            set_settings = yclient.rotor_station_settings2(station = "user:onyourwave", mood_energy = random.choice(random_mood), diversity = random.choice(random_diversity), language = random.choice(random_lang))
            
            #set random value for station onyourwave
            getTrack = yclient.rotor_station_tracks(station = "user:onyourwave", settings2 = set_settings)
            getTrackInfo = random.choice(getTrack["sequence"]) #random choice track
            getTrackId = getTrackInfo["track"]["id"]

            #musicFile download track from yaMusic to PATH_FOR_MUSIC
            yclient.tracks_download_info(track_id=getTrackId)[0].download(file_path + str.capitalize(getTrackInfo["track"]["artists"][0]["name"]) + " - " + str.capitalize(getTrackInfo["track"]["title"]) + ".mp3")
            
            #musicFilePath for client.send_message telegram, send mp3 file.
            musicFilePath = file_path + str.capitalize(getTrackInfo["track"]["artists"][0]["name"]) + " - " + str.capitalize(getTrackInfo["track"]["title"]) + ".mp3"
            print("Путь до файла с музякой: " + musicFilePath)

            #set default value for station onyourwave. If u listen station in realtime its fix set setting for station from bot. 
            yclient.rotor_station_settings2(station = "user:onyourwave", mood_energy ="all" , diversity= "default",  language="any")
            
            return musicFilePath
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (yaMusic_file): " + str(num_retries - attempt_no - 1))
                continue
            else:
                print("API (yaMusic_file) ERROR! " + str(num_retries) + " retries expired!")
                return file_path + os.getenv("MUSIC_EXCEPT")
