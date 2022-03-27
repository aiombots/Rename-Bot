class Scripted(object):    


    PROGRESS_DIS = """\n
╭───[ {0} ]────⍟
│
├<b>📁 : {2} | {3}</b>
│
├<b>🚀 : {1}%</b>
│
├<b>⚡ : {4}/s</b>
│
├<b>⏱️ : {5}</b>
╰─────────────────⍟"""

    HELP_TEXT = """
Sᴇɴᴅ A Pʜᴏᴛᴏ Tᴏ Mᴀᴋᴇ Iᴛ As Tʜᴜᴍʙɴᴀɪʟ (ᴏᴘᴛɪᴏɴᴀʟ)

Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ (ᴏʀ) Mᴇᴅɪᴀ 

Sᴇʟᴇᴄᴛ Tʜᴇ Dᴇsɪʀᴇᴅ Oᴘᴛɪᴏɴ Aɴᴅ Sᴇɴᴅ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ

Tʜᴀᴛs Iᴛ, Wᴀɪᴛ Iᴛ Tᴏ Pʀᴏᴄᴇss

Cᴏᴍᴍᴀɴᴅs -

/start - Tᴏ Sᴛᴀʀᴛ Tʜᴇ Bᴏᴛ

/sthumbnail - Tᴏ Vɪᴇᴡ Yᴏᴜ'ʀᴇ Tʜᴜᴍʙɴᴀɪʟ

/dthumbnail - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜ'ʀᴇ Tʜᴜᴍʙɴᴀɪʟ"""


    ABOUT_TEXT = """
╭────[ Aʙᴏᴜᴛ Uꜱ ]────⍟
│
├ <b>Bᴏᴛ Nᴀᴍᴇ : <a href='https://t.me/AIOM_RENAMER_PRO_BOT'>Rᴇɴᴀᴍᴇʀ Bᴏᴛ</a></b>
│
├ <b>Cʜᴀɴɴᴇʟ : <a href='https://t.me/aiom_bots'>Aɪ๏ᴍ Bᴏᴛs</a></b>
│
├ <b>Vᴇʀsɪᴏɴ : <a href='https://t.me/AIOM_RENAMER_PRO_BOT'>2.9.2 Bᴇᴛᴀ</a></b>
│
├ <b>Sᴏᴜʀᴄᴇ : <a href='https://t.me/AIOM_RENAMER_PRO_BOT'>Cᴏᴍɪɴɢ Sᴏᴏɴ</a></b>
│
├ <b>Sᴇʀᴠᴇʀ : <a href='https://heroku.com'>Hᴇʀᴏᴋᴜ</a></b>
│
├ <b>ʟɪʙʀᴀʀʏ : <a href='https://github.com/pyrogram'>Pʏʀᴏɢʀᴀᴍ</a></b>
│
├ <b>Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'>Pʏᴛʜᴏɴ 3.9.4</a></b>
│
├ <b>Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/ajvadntr2'>محمد اجود</a></b>
│
├ <b>Pᴏᴡᴇʀᴇᴅ Bʏ : <a href='https://t.me/aiom_bots'>Aɪ๏ᴍ Bᴏᴛs</a></b>
│
╰──────[ Tʜᴀɴᴋ Yᴏᴜ ]───⍟"""

    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<b>Aᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ 🚸</b>"
    BANNED_USER_TEXT = "<b>Aᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ 🚸</b>"
    TRYING_TO_UPLOAD = "<b>Uᴩʟᴏᴅɪɴɢ.....</b>"
    CURRENT_THUMBNAIL = "Yᴏᴜ'ʀᴇ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ"
    THUMBNAIL_SAVED = "Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssꜰᴜʟʟʏ  ✓"
    THUMBNAIL_DELETED = "Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssꜰᴜʟʟʏ  ✓"
    NO_THUMBNAIL_FOUND = "No Thumbnail Found"
    TRYING_TO_DOWNLOAD = "<b>Pʀᴏᴄᴇssɪɴɢ....</b>"
    UPLOAD_SUCCESS = "<u><i>Tʜᴀɴᴋs Fᴏʀ Usɪɴɢ ᴍᴇ❤</i></u>"
    REPLY_TO_MEDIA = "<i>Reply to Media For Converting with Command /convert</i>"
    UPLOAD_START = "<b>UPLOADING</b>"
    DOWNLOAD_START = "<b>RENAMEING</b>"
    JOIN_NOW_TEXT = "Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ</b>"
    REPLY_TO_FILE = "<b>Reply to that media with /rename new name .ext</i>"
    CONTACT_MY_DEVELOPER = "<i>Something Went Wrong! Contact in Support @AIOM_BOTS</i>"
    START_TEXT = """<b>Hᴇʟʟᴏ</b> 👋 <b>,  {} ♡

Tʜɪꜱ Iꜱ A Fᴀꜱᴛᴇꜱᴛ Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ Fɪʟᴇ Cᴏɴᴠᴇʀᴛᴇʀ Fᴜᴛᴜʀᴇ & Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ Sᴜᴘᴘᴏʀᴛ

Pʀᴇꜱꜱ Hᴇʟᴩ Bᴜᴛᴛᴏɴ Fᴏʀ Mᴏʀᴇ Iɴꜰᴏ...

Pᴏᴡᴇʀᴇᴅ Bʏ : @AIOM_BOTS</b>"""
    UPGRADE_TEXT = "<b>To upgrade your subscription <a href='https://t.me/ajvadntr'>[Click Here]</a></b>"
