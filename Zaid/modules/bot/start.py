# BADMUSIC/plugins/bot/start.py  (only the reply_photo parts adjusted)
import pyrogram
from pyrogram.errors import BadRequest

# helper to remove user-mention URLs from InlineKeyboardMarkup
def sanitize_markup(markup):
    if not markup:
        return None
    try:
        rows = []
        for row in markup.inline_keyboard:
            new_row = []
            for btn in row:
                # remove buttons that are tg://user?id=... or contain 'start=user' patterns
                if btn.url and ("tg://user?id=" in btn.url or "start=" in (btn.url or "")) and btn.url.startswith("tg"):
                    continue
                new_row.append(btn)
            if new_row:
                rows.append(new_row)
        if not rows:
            return None
        return pyrogram.types.InlineKeyboardMarkup(rows)
    except Exception:
        return None

# usage example where you reply_photo
try:
    markup = InlineKeyboardMarkup(out)
    safe_markup = sanitize_markup(markup) or None
    await message.reply_photo(
        random.choice(IMAGE),
        caption=_["start_2"].format(message.from_user.mention, app.mention),
        reply_markup=safe_markup,
    )
except pyrogram.errors.exceptions.bad_request_400.ButtonUserPrivacyRestricted:
    # send without potentially restricted buttons
    await message.reply_photo(
        random.choice(IMAGE),
        caption=_["start_2"].format(message.from_user.mention, app.mention),
    )
