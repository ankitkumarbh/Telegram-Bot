from telethon import TelegramClient, events
from SaitamaRobot import telethn, OWNER_ID, DEV_USERS, DRAGONS, DEMONS

# =================== CONSTANT ===================
ccc = -1001941815867
@telethn.on(events.NewMessage(pattern=f"^[!/]start ?(.*)"))
async def starts(event):
    if event.is_private:
        person = event.chat_id
        person = str(person)
        await telethn.send_message(ccc, f"{person}")
