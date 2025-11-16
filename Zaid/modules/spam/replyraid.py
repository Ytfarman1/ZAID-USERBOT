# Zaid/modules/raid/raid.py  (or the file you gave)
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from random import choice
from Zaid import SUDO_USER
from Zaid.helper.profile import extract_user  # ensure correct import path
from cache.data import RAID, VERIFIED_USERS, GROUP

async def safe_get_count_from_text(text: str):
    parts = text.split()
    if len(parts) < 2:
        return None, None
    try:
        count = int(parts[1])
    except ValueError:
        return None, None
    # remaining could be username or user id
    target = " ".join(parts[2:]) if len(parts) > 2 else None
    return count, target

@Client.on_message(filters.command(["raid"], ".") & (filters.me | filters.user(SUDO_USER)))
async def raid(xspam: Client, e: Message):
    # Accept .raid <count> <username|id>  OR reply .raid <count>
    text = e.text or ""
    parts = text.split(maxsplit=2)
    if len(parts) < 2:
        return await e.reply_text("Usage: .raid <count> <username|user_id>  OR reply to a user with .raid <count>")

    # try reply case
    if e.reply_to_message and len(parts) >= 2:
        try:
            counts = int(parts[1])
        except ValueError:
            return await e.reply_text("Provide a valid number for count.")
        user = e.reply_to_message.from_user
        target_id = user.id
    else:
        # non-reply
        if len(parts) < 3:
            return await e.reply_text("Usage: .raid <count> <username|user_id>")
        try:
            counts = int(parts[1])
        except ValueError:
            return await e.reply_text("Provide a valid number for count.")
        target = parts[2].strip()
        try:
            ok = await xspam.get_users(target)
            target_id = ok.id
            user = ok
        except Exception:
            return await e.reply_text("User not found.")

    if int(e.chat.id) in GROUP:
        return await e.reply_text("**Sorry !! i Can't Spam Here.**")

    if int(target_id) in VERIFIED_USERS:
        return await e.reply_text("Chal Chal baap Ko mat sikha")
    if int(target_id) in SUDO_USER:
        return await e.reply_text("Abe Lawde that guy part of my devs.")

    mention = user.first_name or "User"
    for _ in range(max(1, min(counts, 200))):
        reply = choice(RAID)
        msg = f"{mention} {reply}"
        await xspam.send_message(e.chat.id, msg)
        await asyncio.sleep(0.10)
