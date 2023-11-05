from telethon import TelegramClient, events
from SaitamaRobot import telethn, OWNER_ID, DEV_USERS, DRAGONS, DEMONS

# =================== CONSTANT ===================

@telethn.on(events.NewMessage(pattern=f"^[!/]start ?(.*)"))
