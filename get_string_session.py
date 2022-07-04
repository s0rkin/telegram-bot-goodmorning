#! /usr/bin/env python3

import os

import dotenv

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

with TelegramClient(StringSession(), os.getenv("TELEGRAM_API_ID"), os.getenv("TELEGRAM_API_HASH")) as client:
    print(client.session.save())
    # Write changes to .env file. DO NOT TEST need testing :)
    os.environ["TELEGRAM_SESSION_STRING"] = client.session.save()
    dotenv.set_key(os.environ["TELEGRAM_SESSION_STRING"])
