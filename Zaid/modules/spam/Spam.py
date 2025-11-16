# Zaid/modules/spam/Spam.py
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message
from random import choice
from cache.data import *  # PORM, GROUP constants etc.
from Zaid import SUDO_USER

usage = "Usage:\n.pornspam <count>\n.hang <count>"

@Client.on_message(
    filters.command(["pornspam"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pornspam(xspam: Client, e: Message):
    # safe parse
    try:
        counts = int(e.command[1])
    except (IndexError, ValueError):
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
        return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    kkk = "**#Pornspam**"
    count = max(1, min(counts, 200))  # limit to avoid abuse
    for _ in range(count):
        prn = choice(PORM)
        try:
            if prn.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                await xspam.send_photo(e.chat.id, prn, caption=kkk)
            elif prn.lower().endswith((".mp4", ".mkv", ".mov")):
                await xspam.send_video(e.chat.id, prn, caption=kkk)
            else:
                await xspam.send_message(e.chat.id, prn)
        except Exception:
            # skip failures
            pass
        await asyncio.sleep(0.4)


@Client.on_message(
    filters.command(["hang"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def hang(xspam: Client, e: Message):
    try:
        counts = int(e.command[1])
    except (IndexError, ValueError):
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
        return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    zaid = "⃟꙰⃟..."  # keep original long string or load from constant
    count = max(1, min(counts, 200))
    for _ in range(count):
        await xspam.send_message(e.chat.id, zaid)
        await asyncio.sleep(0.3)
