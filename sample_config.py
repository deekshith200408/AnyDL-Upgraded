import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1777762862:AAH2nl1wHVIFn_GqVLIRpKVsQg3LmjlIvx0")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 2980496))
    API_HASH = os.environ.get("API_HASH","9415a61fedcc0f00f33667ca46e577a3")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "1086432320").split())
    # reg: Procedures
    UTUBE_BOT_USERS =  set(str(x) for x in os.environ.get("UTUBE_BOT_USERS", "").split())
    SUPER_DLBOT_USERS =  set(str(x) for x in os.environ.get("SUPER_DLBOT_USERS", "").split())
    SUPER3X_DLBOT_USERS =  set(str(x) for x in os.environ.get("SUPER3X_DLBOT_USERS", "").split())
    SUPER7X_DLBOT_USERS =  set(str(x) for x in os.environ.get("SUPER7X_DLBOT_USERS", "").split())
    BANNED_USERS =  set(str(x) for x in os.environ.get("BANNED_USERS", "").split())
    # Wat was I thinking? :\
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # for storing the user details
    DB_SQLALCHEMY = "USERS.session"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = "lcJyZwbl"
    # for Google Custom Search Engine
    GCS_API_KEY = os.environ.get("GCS_API_KEY", None)
    GCS_SE_ID = os.environ.get("GCS_SE_ID", None)
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # dict to hold Google Drive SignIns
    G_DRIVE_AUTH_DRQ = {}
