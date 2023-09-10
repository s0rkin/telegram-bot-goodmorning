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
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (yaMusic_chart): " + str(num_retries - 1))
                yclient = yaMusic_chart(num_retries - 1)
            else:
                print("Yandex API error: unavailable chart! " + str(num_retries) + " retries expired!")
                pass
        return chartTrack

def yaMusic_file(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            yclient = yaClient(os.getenv("YANDEX_TOKEN")).init()

            music = yclient.users_likes_tracks()[0].fetch_track()
            getTrack = yclient.rotor_station_tracks(station='user:onyourwave')
            getTrackInfo = getTrack["sequence"][random.randint(0,4)] #random track from onyourwave. (onyourwave send only 5 tracks, random it 1-5)
            getTrackId = getTrackInfo["track"]["id"]
            musicFile = yclient.tracks_download_info(track_id=getTrackId)[0].download(file_path + str.capitalize(getTrackInfo["track"]["artists"][0]["name"]) + " - " + str.capitalize(getTrackInfo["track"]["title"]) + '.mp3')
            musicFilePath = file_path + str.capitalize(getTrackInfo["track"]["artists"][0]["name"]) + " - " + str.capitalize(getTrackInfo["track"]["title"]) + '.mp3'
            print("Путь до файла с музякой: " + musicFilePath)
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (yaMusic_file): " + str(num_retries - 1))
                yclient = yaMusic_file(num_retries - 1)
            else:
                print("API (yaMusic_file) ERROR! " + str(num_retries) + " retries expired!")
                pass
                #TODO: need return random mp3 file from /home/user + text if api error or something got error.
        return musicFilePath