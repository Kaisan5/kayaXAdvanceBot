

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8154426339")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002170811388")) #Your db channel Id
OWNER = os.environ.get("OWNER", "") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "7654385403")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Kurumi:103oq6MdbXWdyI4A@cluster0.yfn0lmh.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "0"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://telegra.ph/You-Are-Stalker-Stay-Away-From-Us-05-12")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>Hᴇʟʟᴏ!! Wᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</a> Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ\n\nHᴇʟᴘʟɪɴᴇ @EternalsHelplineBot\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈sᴜᴘʀᴇᴀᴍ: <a href=https://t.me/Stelleron_Hunter>sᴛᴇʟʟᴇʀᴏɴ</a>\n◈ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Eternals>ᴇᴛᴇʀɴᴀʟs</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢs : <a href=https://t.me/+VxWwaMA6g_JkNTA9>ᴏɴɢᴏɪɴɢ</a>\n◈ᴇᴄᴄʜɪ ᴅᴇx : <a href=https://t.me/Ecchi_Dex>ᴇᴄᴄʜɪ</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href=https://t.me/EternalsHelplineBot>ʜᴇʟᴘʟɪɴᴇ</a></blockquote expandable></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>Hᴇʏ! {mention} Wᴇʟᴄᴏᴍᴇ Tᴏ Cᴏᴍᴍᴜɴɪᴛʏ Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ʏᴏᴜ ᴄᴀɴ ᴅᴏ sᴏ ʙʏ sᴜʙsᴄʀɪʙɪɴɢ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ</blockquote></a>\n<blockquote expandable></a>Gᴜɪᴅᴇ Tᴏ Wᴀᴛᴄʜ Vɪᴅᴇᴏ Wɪᴛʜ Sᴜʙᴛɪᴛʟᴇs Iғ Sᴜʙᴛɪᴛʟᴇs Nᴏᴛ Sʜᴏᴡɪɴɢ\n</a>❏ ᴛᴜᴛᴏʀɪᴀʟ\n</a>├ <a href=https://telegra.ph/HOW-TO-WATCH-04-20-3>Cʟɪᴄᴋ Hᴇʀᴇ </a>\n❏ Hᴇʟᴘʟɪɴᴇ Bᴏᴛ</a>\n├ <a href=https://t.me/EternalsHelplineBot>Hᴇʟᴘʟɪɴᴇ </a>\nTʜᴀɴᴋs Fᴏʀ ʏᴏᴜʀ Sᴜᴘᴘᴏʀᴛ</blockquote expandable></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><blockquote>Hᴇʟʟᴏ!! {first} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</blockquote></a> Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ʙᴏᴛ ᴀɢᴀɪɴ,Fᴏʀ Oɴɢᴏɪɴɢ Aɴɪᴍᴇ ~ <a href=https://t.me/Anime_Ongoing_Airing>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢ </a></b>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
"""
#--------------------------------------------
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = True if os.environ.get('CUSTOM_CAPTION', "False") == "True" else False
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @Stelleron_Hunter !!\n\n👋Hᴇʏ Fʀɪᴇɴᴅ,🚫Dᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇs ᴛᴏ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ I'ᴍ ᴏɴʟʏ Fɪʟᴇ Sʜᴀʀᴇ ʙᴏᴛ!"
#--------------------------------------------


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
   
