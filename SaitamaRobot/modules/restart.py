import os
import asyncio
import sys
import time
from telethon import events
from os import environ
from telethon.sync import TelegramClient
from SaitamaRobot import telethn, OWNER_ID
OWNER_ID = [859187586, 5708353495]

heroku_api = "https://api.heroku.com"
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
appname = os.environ.get("HEROKU_APP_NAME", None)
@telethn.on(events.NewMessage(pattern=f"^[!/]restart ?(.*)"))
async def restart(event):
    if event.chat_id not in OWNER_ID:
        return
    if HEROKU_API_KEY:
        os.system("pip3 install heroku3")
        import heroku3
        await event.respond("`Bot Restarting.....`")
        heroku_conn = heroku3.from_key(HEROKU_API_KEY)
        app = heroku_conn.apps()[appname]
        app.restart()
