#! /usr/bin/env python3

import os
import dotenv

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

with TelegramClient(StringSession(), os.getenv("TELEGRAM_API_ID"), os.getenv("TELEGRAM_API_HASH")) as client:
    print(client.session.save())
    # Write changes to .env file.
    os.environ["TELEGRAM_STRING_SESSION"] = client.session.save()
    dotenv.set_key(dotenv_file, "TELEGRAM_STRING_SESSION", os.environ["TELEGRAM_STRING_SESSION"])