class Scripted(object):    


    PROGRESS_DIS = """\n
╭──────[{0}]────⍟
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
<i>𝐖𝐚𝐭𝐜𝐡 𝐕𝐢𝐝𝐞𝐨 𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐌𝐞 <a href='https://youtu.be/HnXdu74o34E'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></i>\n
<i>𝐒𝐞𝐧𝐝 𝐚 𝐩𝐡𝐨𝐭𝐨 𝐭𝐨 𝐦𝐚𝐤𝐞 𝐢𝐭 𝐚𝐬 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 (optional)</i>\n
<i>𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 (or) 𝐌𝐞𝐝𝐢𝐚 𝐟𝐫𝐨𝐦 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦</i>\n
<i>𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧𝐭𝐨 𝐯𝐢𝐝𝐞𝐨 𝐮𝐬𝐞 /convert 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐟𝐢𝐥𝐞 𝐰𝐢𝐭𝐡 /rename 𝐧𝐞𝐰 𝐧𝐚𝐦𝐞.ext</i>\n
<i>𝐕𝐢𝐞𝐰 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /sthumbnail 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐃𝐞𝐥𝐞𝐭𝐞 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /dthumbnail 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>"""


    ABOUT_TEXT = """
╭────[🔅Rᴇɴᴀᴍᴇʀ Bᴏᴛ🔅]───⍟
│
├<b>🤖 Bot Name : <a href='https://t.me/teleroid_renamer_bot'>Rename X2 Bot</a></b>
│
├<b>📢 Channel : <a href='https://t.me/TeleRoidGroup'>@TeleRoidGroup</a></b>
│
├<b>👥 Version : <a href='https://t.me/TeleRoid_Renamer_bot'>0.9.2 beta</a></b>
│
├<b>💢 Source : <a href='https://github.com/PredatorHackerzZ/Renamer-bot'>Click Here</a></b>
│
├<b>🌐 Server : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
│
├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>
│
├<b>👨‍💻 Developer : <a href='https://t.me/PredatorHackerZ'>Pred∆tor</a></b>
│
├<b>🚸 Powered By : <a href='https://t.me/Moviesflixers_DL'>@HindiWebNetwork</a></b>
│
╰──────[Thanks 😊]───⍟"""

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
