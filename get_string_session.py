#! /usr/bin/env python3

import os

from dotenv import load_dotenv

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

with TelegramClient(StringSession(), os.getenv("TELEGRAM_API_ID"), os.getenv("TELEGRAM_API_HASH")) as client:
    print(client.session.save())
