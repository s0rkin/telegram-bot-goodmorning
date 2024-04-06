#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Jul 4, 2022
# Links       : https://github.com/s0rkin/
# version ='2.1'
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
    error_return = 0
    if error_return == 0:
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
                    print("CURRENT RETRY (yaMusic_chart): " + str(num_retries))
                    num_retries += -1
                    continue
                else:
                    print("Yandex API error: unavailable chart! 10 retries expired!")
                    error_return += 1
                    break
    else:
        return "Yandex API error: unavailable chart!"

def yaMusic_file(num_retries = 10):
    error_return = 0
    if error_return == 0:
        for attempt_no in range(num_retries):
            try:
                yclient = yaClient(os.getenv("YANDEX_TOKEN")).init()

                #SETING'S for onyourwave yamusic! 
                #available setting's for mood_energy: fun, active, calm, sad, all.
                #available setting's for diversity: favorite, popular, discover, default.
                #available setting's for language: not-russian, russian, any.

                setStation = yclient.rotor_station_settings2(station = "user:onyourwave", mood_energy = "active", diversity = "popular", language = "any")
                print(setStation)
                #FETCH last track for getTrack.
                #music = yclient.users_likes_tracks()[0].fetch_track()
                getTrack = yclient.rotor_station_tracks(station = "user:onyourwave", settings2 = True)
                getTrackInfo = getTrack["sequence"][random.randint(0,4)] #random track from onyourwave. (onyourwave send only 5 tracks, random it 1-5)
                getTrackId = getTrackInfo["track"]["id"]

                #musicFile download track from yaMusic to PATH_FOR_MUSIC
                musicFile = yclient.tracks_download_info(track_id=getTrackId)[0].download(file_path + str.capitalize(getTrackInfo["track"]["artists"][0]["name"]) + " - " + str.capitalize(getTrackInfo["track"]["title"]) + ".mp3")

                #musicFilePath for client.send_message telegram, send mp3 file.
                musicFilePath = file_path + str.capitalize(getTrackInfo["track"]["artists"][0]["name"]) + " - " + str.capitalize(getTrackInfo["track"]["title"]) + ".mp3"
                print("Путь до файла с музякой: " + musicFilePath)

                return musicFilePath
            except:
                if attempt_no < (num_retries - 1):
                    time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                    print("CURRENT RETRY (yaMusic_file): " + str(num_retries))
                    num_retries += -1
                    continue
                else:
                    print("API (yaMusic_file) ERROR! 10 retries expired!")
                    error_return += 1
                    break
    else:
        return file_path + os.getenv("MUSIC_EXCEPT") #need fix for playing in telegram
            #TODO: need return random mp3 file from /home/user + text if api error or something got error.