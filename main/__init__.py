from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "28938535"  ( default=None, cast=int)
API_HASH = config("API_HASH", "7b3be0a2d8c16bc23d340da4748b12ae" default=None)
BOT_TOKEN = config("BOT_TOKEN", "7755169706:AAF4yb7XbvL8SsJHbcpnx_p5Q-vd8kpjERY" default=None)
BOT_UN = config("BOT_UN", "Averilz_compbot" default=None)
AUTH_USERS = config("AUTH_USERS", default=None, cast=int)
LOG_CHANNEL = config("LOG_CHANNEL", default=None)
LOG_ID = config("LOG_ID", default=None)
FORCESUB = config("FORCESUB", default=None)
FORCESUB_UN = config("FORCESUB_UN", default=None)
ACCESS_CHANNEL = config("ACCESS_CHANNEL", default=None)
MONGODB_URI = config("MONGODB_URI", default=None)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
