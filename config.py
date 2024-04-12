#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21944530"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0b629e4827bd82816a5959211618902a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-100"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "asiknyamedia")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1928851198"))

#Port
PORT = os.environ.get("PORT", "8014")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://botvtm:Rizqi1687.@atlascluster.y9vs3uq.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
DB_NAME = os.environ.get("DATABASE_NAME", "botvtm")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-100"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-100"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>{first}\n\n</b>")
try:
    ADMINS=[1928851198]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", " Hello {first}\n\n<b>Anda harus bergabung di Channel/Grup saya untuk menggunakan saya</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b> 𝟿 ɢʀᴜᴘ ᴠᴠɪᴘ ᴄᴜᴍᴀ 𝟸𝟻ᴋ

ᴋᴇᴜɴᴛᴜɴɢᴀɴ ᴠᴠɪᴘ
- ɴᴏɴᴛᴏɴ ᴛᴀɴᴘᴀ ʟɪɴᴋ
- ʙᴇʀɪsɪ ʀɪʙᴜᴀɴ ᴠɪᴅᴇᴏ
- ᴜᴘᴅᴀᴛᴇ ᴛᴇʀᴜs ᴛɪᴀᴘ ʜᴀʀɪ

ᴠᴠɪᴘ ɪɴᴅᴏ
ᴠᴠɪᴘ ʙᴏᴄɪʟ
ᴠᴠɪᴘ ʜɪᴊᴀʙ
ᴠᴠɪᴘ ᴊᴀᴠ
ᴠᴠɪᴘ ᴛᴀʟᴇɴᴛ
ᴠᴠɪᴘ ᴄᴏʟᴍᴇᴋ
ᴠᴠɪᴘ ᴘᴇʟᴀᴊᴀʀ
ᴠᴠɪᴘ ʟᴇsʙɪ
ᴠᴠɪᴘ ɢᴀɴɢʙᴀɴɢ

ᴘᴀʏᴍᴇɴᴛ
- ǫʀɪs
- ᴅᴀɴᴀ
- ɢᴏᴘᴀʏ
- ᴏᴠᴏ
- sʜᴏᴘᴇᴘᴀʏ
- ᴍ ʙᴀɴᴋɪɴɢ

ᴊᴏɪɴ ᴄᴏɴᴛᴀᴄᴛ @asiknyamedia

ᴊᴏɪɴ ᴏᴛᴏᴍᴀᴛɪs @asiknyamediabot

ᴛᴇsᴛɪ @testijoinvvipnya </b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = ""

ADMINS.append(OWNER_ID)
ADMINS.append(1928851198)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
