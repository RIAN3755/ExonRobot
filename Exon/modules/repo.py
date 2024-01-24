# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi1M
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Exon import Abishnoi as pbot

ABISHNOIX = "https://telegra.ph/file/dc612eb9728ee91c7f9dd.jpg"


@pbot.on_cmd("repo")
async def repo(_, message):
    await message.reply_photo(
        photo=ABISHNOIX,
        caption=f"""✨ **ʜᴇʏ {message.from_user.mention},**

**ᴏᴡɴᴇʀ  : [𝑨𝒚𝒂𝒏𝒐](https://t.me/Call_me_ayano)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ɴᴇᴛᴡᴏʀᴋ•", url="https://t.me/Eternal_society"
                    ),
                    InlineKeyboardButton(
                        "•ꜱᴜᴘᴘᴏʀᴛ•", url="https://t.me/beerussupportchat"
                    ),
                ]
            ]
        ),
    )
