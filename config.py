import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "24845544"
API_HASH = "57f32b90d5406552ab9156f6404fe5a8"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7073582508:AAHnH4q54GzFqxdcOSwu3aMoJ2apyuX1tfQ"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://github9210:ieMwBAIuNl2NEMRO@cluster0.lcwkg5r.mongodb.net/?retryWrites=true&w=majority"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 6000))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002064111110

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = 6257927828

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/koreansmu/StormVortexLv2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/storm_techh")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/storm_core")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2d3fd5ccdd3d43dda6f17864d8eb7281")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "48d311d8910a4531ae81205e1f754d27")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQF37cIAFMBWpYCTsAHMEvvVD1Nrn2omYdDMCGGIe5mJCcEye44awozXzZzzPWccHDE7upUzTUHH3OEFHYFv7n99HsStvJWSO2HU29PRBZS9mEqgrS6hdqSZjkra4Xli56tfrdHvdW9HFH5PzpqMCctVFy9UCSv_qdxBr83Os50LP6aAtV5LQXfnd4O0sZ1OHb8DZAorAB6hjERyzutjnWIwVkSME_-Ex12YMQB3d7AHfURgoaJaOqMF4IwUQzHZR58WZfTzC8Cn7r81oOYP7vmKMn7GLd_42clnzW7NvhUfFS2f6e-5eNeAra9pkFSRY-y0S4H00PGfqAAZVkexvSLYapp0agAAAAG3FNOBAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/7438999f48faad861f81c-cc25c52ab50faab989.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/d259a18ae576e95cbffed-566e0e7cfc4f0340b0.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph//file/0879fbdb307005c1fa8ab.jpg"
STATS_IMG_URL = "https://telegra.ph//file/72e4414f618111ea90a57.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph//file/ab4925a050e07b00f63c5.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph//file/3b59b15e1914b4fa18b71.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )