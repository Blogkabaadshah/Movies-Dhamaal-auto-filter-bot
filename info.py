import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '25680646'))
API_HASH = environ.get('API_HASH', '0a403b1d2ac0aa5ba34a2fab2ba6a12b')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6964743059').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/MDadminking')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002188008502'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002443223307').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://podcastlemon64:X2gbX07xKWK7lWVG@movieguru.lqw6s.mongodb.net/?retryWrites=true&w=majority&appName=Movieguru")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://Blog:eCXh29bITQQS0rrm@cluster0.s1aaq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Movieguru")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'cluster0')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002188008502'))
QR_CODE = environ.get('QR_CODE', 'https://t.me/c/2443223307/9')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002188008502'))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002188008502'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Moviegurusupport/9")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/Moviegurusupport/8")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/Moviegurusupport/5")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://t.me/c/2443223307/6")
SHORTENER_API = environ.get("SHORTENER_API", "7c7829c84feab901e52fbbdb34bc45dd50b3c56d")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "publicearn.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "19df554dcfbb6b33544301d6618e0ce6ca3084c1")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "gplinks.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "e13d1324ecdd75f04a0ab5ead11d52d215585abd")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "omegalinks.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "3600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002466967695')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002489973303'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', False)
