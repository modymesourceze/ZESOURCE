import time
import os, sys
os.system("pip install Telethon")
os.system("pip install telethon-session-sqlalchemy")
os.system("pip install setuptools")
os.system("pip install wheel")
os.system("pip install aiocsv")
os.system("pip install aiofiles")
os.system("pip install aiohttp==3.9.5")
os.system("pip install aiosqlite")
os.system("pip install arabic_reshaper")
os.system("pip install beautifulsoup4")
os.system("pip install cloudscraper")
os.system("pip install psycopg2")
os.system("pip install colour")
os.system("pip install cowpy")
os.system("pip install DateTime")
os.system("pip install emoji==1.7.0")
os.system("pip install ffmpeg-python")
os.system("pip install geopy")
os.system("pip install gitpython")
os.system("pip install google-api-python-client")
os.system("pip install google-auth-httplib2")
os.system("pip install google-auth-oauthlib")
os.system("pip install googletrans==3.1.0a0")
os.system("pip install gtts")
os.system("pip install hachoir")
os.system("pip install heroku3")
os.system("pip install html-telegraph-poster")
os.system("pip install httpx[http2]")
os.system("pip install humanize")
os.system("pip install ipaddress")
os.system("pip install img2html")
os.system("pip install jikanpy")
os.system("pip install justwatch")
os.system("pip install kvsqlite")
os.system("pip install lottie")
os.system("pip install lyricsgenius")
os.system("pip install markdown")
os.system("pip install motor")
os.system("pip install moviepy")
os.system("pip install nekos.py")
os.system("pip install opentele")
os.system("pip install Pillow")
os.system("pip install prettytable")
os.system("pip install psutil")
os.system("pip install psycopg2")
os.system("pip install py-tgcalls==0.9.7")
os.system("pip install pyfiglet")
os.system("pip install PyGithub")
os.system("pip install pygments")
os.system("pip install pylast")
os.system("pip install pymediainfo")
os.system("pip install pyquery")
os.system("pip install pyrogram")
os.system("pip install pySmartDL")
os.system("pip install python-barcode")
os.system("pip install python-dotenv")
os.system("pip install pytz")
os.system("pip install qrcode")
os.system("pip install regex")
os.system("pip install requests")
os.system("pip install search-engine-parser")
os.system("pip install selenium")
os.system("pip install spamwatch")
os.system("pip install speedtest-cli")
os.system("pip install sqlalchemy-json")
os.system("pip install sqlalchemy==1.3.23")
os.system("pip install telegraph")
os.system("pip install tgcrypto")
os.system("pip install ujson")
os.system("pip install urlextract")
os.system("pip install user_agent")
os.system("pip install validators")
os.system("pip install vcsi")
os.system("pip install wand")
os.system("pip install wget")
os.system("pip install youtube-search-python==1.4.9")
os.system("pip install youtube-search")
os.system("pip install youtube_dl")
os.system("pip install yt-dlp")

import heroku3

from .Config import Config
from .core.logger import logging
from .core.session import mody
from .sql_helper.globals import addgvar, delgvar, gvarstatus

__version__ = "3.1.3"
__license__ = "كـتابة وتـعديل فريـق زد إي"
__author__ = "زد إي <https://T.ME/UI_XB>"
__copyright__ = "ZE TEAM (C) 2023 - 2024  " + __author__

mody.version = __version__
mody.tgbot.version = __version__
LOGS = logging.getLogger("UI_XB")
bot = mody

StartTime = time.time()
JEPVERSION = "3.1.3"


if Config.UPSTREAM_REPO == "SourceZe":
    UPSTREAM_REPO_URL = "https://github.com/modymesourceze/ZESOURCE"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        Config.BOTLOG = False
        Config.BOTLOG_CHATID = "me"
    else:
        Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.BOTLOG = True
else:
    if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":
        Config.BOTLOG_CHATID = int("-" + str(Config.PRIVATE_GROUP_BOT_API_ID))
    else:
        Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
    Config.BOTLOG = True

if Config.PM_LOGGER_GROUP_ID == 0:
    if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        Config.PM_LOGGER_GROUP_ID = -100
    else:
        Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
    Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))
try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None


# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}

# Variables
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID
PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID
