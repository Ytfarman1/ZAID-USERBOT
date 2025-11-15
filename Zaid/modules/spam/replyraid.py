import asyncio
from pyrogram import filters, Client
from Zaid.modules.help import *
from Zaid.helper.utility import get_arg
from pyrogram.types import *
from pyrogram import __version__
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from Zaid.database.rraid import *
from Zaid import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(1669178360)
from Zaid.helper.PyroHelpers import get_ub_chats
from Zaid.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
RAIDS = []

# ======================================================
# ✔ FIXED PORNSPAM
# ======================================================
@Client.on_message(
    filters.command(["pornspam"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def porn_spam(xspam: Client, e: Message): 
    
    if len(e.command) < 2:
        return await e.reply_text("Usage: .pornspam <count>")

    try:
        count = int(e.command[1])
    except:
        return await e.reply_text("Count must be a number!")

    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")

    kkk = "**#Pornspam**"

    for _ in range(count):
         prn = choice(PORM)
         if ".jpg" in prn or ".png" in prn:
              await xspam.send_photo(e.chat.id, prn, caption=kkk)
         elif ".mp4" in prn or ".MP4" in prn:
              await xspam.send_video(e.chat.id, prn, caption=kkk)
         await asyncio.sleep(0.4)



# ======================================================
# ✔ FIXED HANG
# ======================================================
@Client.on_message(
    filters.command(["hang"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def hang(xspam: Client, e: Message): 

    if len(e.command) < 2:
        return await e.reply_text("Usage: .hang <count>")

    try:
        count = int(e.command[1])
    except:
        return await e.reply_text("Count must be a number!")

    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")

    zaid = "⃟꙰" * 500  # same style, reduced duplicates

    for _ in range(count):
         await xspam.send_message(e.chat.id, zaid)
         await asyncio.sleep(0.3)



# ======================================================
# ✔ FIXED RAID
# ======================================================
@Client.on_message(
    filters.command(["raid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def raid(xspam: Client, e: Message):  
    
      if len(e.command) < 3 and not e.reply_to_message:
          return await e.reply_text("Usage: .raid <count> <username>")

      # CASE 1: reply mode
      if e.reply_to_message:
          try:
              counts = int(e.command[1])
          except:
              return await e.reply_text("Count must be a number!")
          user_id = e.reply_to_message.from_user.id

      # CASE 2: normal mode
      else:
          try:
              counts = int(e.command[1])
              target = e.command[2]
          except:
              return await e.reply_text("Usage: .raid <count> <username>")

          ok = await xspam.get_users(target)
          user_id = ok.id

      if int(e.chat.id) in GROUP:
           return await e.reply_text("**Sorry !! i Can't Spam Here.**")

      if int(user_id) in VERIFIED_USERS:
            return await e.reply_text("Chal Chal baap Ko mat sikha")

      if int(user_id) in SUDO_USERS:
            return await e.reply_text("Abe Lawde that guy part of my devs.")

      ok = await xspam.get_users(user_id)
      fname = ok.first_name
      mention = f"[{fname}](tg://user?id={user_id})"

      for _ in range(counts):
            reply = choice(RAID)
            msg = f"{mention} {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.10)



add_command_help(
    "raid",
    [
        [".raid", "<user id and count>`."],
        [".pornspam", "<count>`."],
        [".hang", "Make telegram hang."],
    ],
)


# ======================================================
# 🔥 replyraid disabling command (no change needed)
# ======================================================

@Client.on_message(
    filters.command(["dreplyraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return
    try:
        if user.id not in (await get_rraid_users()):
           await ex.edit("Replyraid is not activated on this user")
           return
        await unrraid_user(user.id)
        RAIDS.remove(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) DeActivated ReplyRaid!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


add_command_help(
    "replyraid",
    [
        [".replyraid", "Reply To User\n To Raid on Someone."],
        [".dreplyraid", "To Disable ReplyRaid."],
    ],
)
