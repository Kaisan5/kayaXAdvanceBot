import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) #Your db channel Id
OWNER = os.environ.get("OWNER", "") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "7654385403")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://WarDevil:vz0Q8jIn5o6xhO82@cluster0.rh2msvd.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/EternalsHelplineBot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "")
FORCE_PIC = os.environ.get("FORCE_PIC", "")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "linkshortify.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 20)) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","https://t.me/+wekKcN1tjbAxY2U1")
SHORT_MSG = "<b><blockquote>𝗬𝗼𝘂𝗿 𝘁𝗼𝗸𝗲𝗻 𝗵𝗮𝘀 𝗲𝘅𝗽𝗶𝗿𝗲𝗱. 𝗣𝗹𝗲𝗮𝘀𝗲 𝗿𝗲𝗳𝗿𝗲𝘀𝗵 𝘆𝗼𝘂𝗿 𝘁𝗼𝗸𝗲𝗻 𝘁𝗼 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲..<a>\nHᴇʟᴘʟɪɴᴇ ʙᴏᴛ @EternalsHelplineBot</blockquote></a>\nTᴏᴋᴇɴ Tɪᴍᴇᴏᴜᴛ: {get_exp_time(VERIFY_EXPIRE)}\n\nᴡʜᴀᴛ ɪs ᴛʜᴇ ᴛᴏᴋᴇɴ??</b>\n\nᴛʜɪs ɪs ᴀɴ ᴀᴅs ᴛᴏᴋᴇɴ. ᴘᴀssɪɴɢ ᴏɴᴇ ᴀᴅ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ ғᴏʀ {get_exp_time(VERIFY_EXPIRE)}\n\nAPPLE/IPHONE USERS COPY TOKEN LINK AND OPEN IN CHROME BROWSER</a>\n<blockquote expandable></a>𝗪𝗲 𝗮𝗿𝗲 𝗮𝗱𝗱𝗶𝗻𝗴 𝗮 𝘁𝗼𝗸𝗲𝗻 𝘀𝘆𝘀𝘁𝗲𝗺. 𝗦𝗼 𝘁𝗵𝗮𝘁 𝗼𝘂𝗿 𝘄𝗼𝗿𝗸 𝗰𝗮𝗻 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲 𝗹𝗶𝗸𝗲 𝘁𝗵𝗶𝘀. 𝗕𝗲𝗰𝗮𝘂𝘀𝗲 𝘄𝗲 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗲𝗮𝗿𝗻𝗶𝗻𝗴 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗯𝘆 𝗱𝗼𝗶𝗻𝗴 𝘁𝗵𝗶𝘀 𝗮𝗹𝗹, 𝘁𝗵𝗮𝘁 𝗶𝘀 𝘄𝗵𝘆 𝘄𝗲 𝗮𝗿𝗲 𝗮𝗱𝗱𝗶𝗻𝗴 𝗮 𝘁𝗼𝗸𝗲𝗻 𝘀𝘆𝘀𝘁𝗲𝗺. 𝗜 𝗵𝗼𝗽𝗲 𝘆𝗼𝘂 𝗴𝘂𝘆𝘀 𝘄𝗶𝗹𝗹 𝘀𝘁𝗶𝗹𝗹 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝘂𝘀.</blockquote expendable></b>"

SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://litter.catbox.moe/5lspqm.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote><a>Hᴇʟʟᴏ!! Wᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</a></b></blockquote></a><b><blockquote><a> Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ\n\nHᴇʟᴘʟɪɴᴇ @EternalsHelplineBot\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!</a></b></blockquote>"
ABOUT_TXT = "<b><blockquote><a>◈sᴜᴘʀᴇᴀᴍ: <a href=https://t.me/Stelleron_Hunter>sᴛᴇʟʟᴇʀᴏɴ</a>\n◈ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Eternals>ᴇᴛᴇʀɴᴀʟs</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢs : <a href=https://t.me/+VxWwaMA6g_JkNTA9>ᴏɴɢᴏɪɴɢ</a>\n◈ᴇᴄᴄʜɪ ᴅᴇx : <a href=https://t.me/Ecchi_Dex>ᴇᴄᴄʜɪ</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href=https://t.me/EternalsHelplineBot>ʜᴇʟᴘʟɪɴᴇ</a></blockquote expandable></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote><a>Hᴇʏ! {mention} Wᴇʟᴄᴏᴍᴇ Tᴏ Cᴏᴍᴍᴜɴɪᴛʏ Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ʏᴏᴜ ᴄᴀɴ ᴅᴏ sᴏ ʙʏ sᴜʙsᴄʀɪʙɪɴɢ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ</a>/blockquote></b></a>\n<blockquote expandable></a>Gᴜɪᴅᴇ Tᴏ Wᴀᴛᴄʜ Vɪᴅᴇᴏ Wɪᴛʜ Sᴜʙᴛɪᴛʟᴇs Iғ Sᴜʙᴛɪᴛʟᴇs Nᴏᴛ Sʜᴏᴡɪɴɢ\n</a>❏ ᴛᴜᴛᴏʀɪᴀʟ\n</a>├ <a href=https://telegra.ph/HOW-TO-WATCH-04-20-3>Cʟɪᴄᴋ Hᴇʀᴇ </a>\n❏ Hᴇʟᴘʟɪɴᴇ Bᴏᴛ</a>\n├ <a href=https://t.me/EternalsHelplineBot>Hᴇʟᴘʟɪɴᴇ </a>\nTʜᴀɴᴋs Fᴏʀ ʏᴏᴜʀ Sᴜᴘᴘᴏʀᴛ</a></blockquote expandable></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><blockquote><a>Hᴇʟʟᴏ!! {first} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</a></blockquote></b></a><b><a>Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ʙᴏᴛ ᴀɢᴀɪɴ,Fᴏʀ Oɴɢᴏɪɴɢ Aɴɪᴍᴇ ~ <a href=https://t.me/Anime_Ongoing_Airing>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢ</a></b>")

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
<b>›› /addpremium :</b> ᴀᴅᴅ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ
<b>›› /premium_users :</b> ʟɪsᴛ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀs
<b>›› /remove_premium :</b> ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ ꜰʀᴏᴍ ᴀ ᴜꜱᴇʀ
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs
<b>›› /count :</b> ᴄᴏᴜɴᴛ verifications
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @nova_flix</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @EternalsHelplineBot !!\n\n👋Hᴇʏ Fʀɪᴇɴᴅ,🚫Dᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇs ᴛᴏ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ I'ᴍ ᴏɴʟʏ Fɪʟᴇ Sʜᴀʀᴇ ʙᴏᴛ!"
#==========================(BUY PREMIUM)====================#
OWNER_TAG = os.environ.get("OWNER_TAG", "EternalsHelplineBot")
UPI_ID = os.environ.get("UPI_ID", "EternalsHelplineBot")
QR_PIC = os.environ.get("QR_PIC", "https://litter.catbox.moe/5lspqm.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/EternalsHelplineBot")
#--------------------------------------------
#Time and its price
#1 Month
PRICE1 = os.environ.get("PRICE1", "29 rs")
#3 Month
PRICE2 = os.environ.get("PRICE2", "99 rs")
#6 Month
PRICE3 = os.environ.get("PRICE3", "299 rs")
#1 Year
PRICE4 = os.environ.get("PRICE4", "399 rs")

#===================(END)========================#

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
   
