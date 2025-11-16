# Zaid/__init__.py
from pyrogram import Client
from config import (
    API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN,
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4,
    STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8,
    STRING_SESSION9, STRING_SESSION10
)
from datetime import datetime
import time
import asyncio
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS.copy() if isinstance(SUDO_USERS, list) else list(SUDO_USERS or [])
clients = []
ids = []

# ensure owner in sudo
if OWNER_ID and OWNER_ID not in SUDO_USER:
    SUDO_USER.append(OWNER_ID)

# lazy aiosession
_aiosession = None
def get_aio_session():
    global _aiosession
    if _aiosession is None or _aiosession.closed:
        _aiosession = ClientSession()
    return _aiosession

# App (bot) instance
app = Client(
    name="app",
    api_id=API_ID or "6435225",
    api_hash=API_HASH or "4e984ea35f854762dcde906dce426c2d",
    bot_token=BOT_TOKEN or None,
    plugins=dict(root="Zaid/modules/bot"),
    in_memory=True,
)

# helper to create user clients lazily (do NOT start them here)
def make_user_client(name, session_string):
    return Client(name=name, api_id=app.api_id, api_hash=app.api_hash, session_string=session_string, plugins=dict(root="Zaid/modules"))

# create clients list based on available strings
if STRING_SESSION1:
    clients.append(make_user_client("one", STRING_SESSION1))
if STRING_SESSION2:
    clients.append(make_user_client("two", STRING_SESSION2))
if STRING_SESSION3:
    clients.append(make_user_client("three", STRING_SESSION3))
if STRING_SESSION4:
    clients.append(make_user_client("four", STRING_SESSION4))
if STRING_SESSION5:
    clients.append(make_user_client("five", STRING_SESSION5))
if STRING_SESSION6:
    clients.append(make_user_client("six", STRING_SESSION6))
if STRING_SESSION7:
    clients.append(make_user_client("seven", STRING_SESSION7))
if STRING_SESSION8:
    clients.append(make_user_client("eight", STRING_SESSION8))
if STRING_SESSION9:
    clients.append(make_user_client("nine", STRING_SESSION9))
if STRING_SESSION10:
    clients.append(make_user_client("ten", STRING_SESSION10))
