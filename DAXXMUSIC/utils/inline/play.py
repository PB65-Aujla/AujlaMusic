import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from DAXXMUSIC import app
from DAXXMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bikash = math.floor(percentage)
    if 0 < bikash <= 10:
        bar = "웃✎........✉유"
    elif 10 < bikash < 20:
        bar = "웃ʰᵉˡˡᵒ..✆...ʰⁱⁱ유"
    elif 20 <= bikash < 30:
        bar = "웃ᵏⁱᵛᵉ ᵒᵒᵒ.❥.ᵇʸᵉ유"
    elif 30 <= bikash < 40:
        bar = "•.¸웃ᶠᵒʳ💍ʸᵒᵘ유¸.•"
    elif 40 <= bikash < 50:
        bar = "‎‎‎ ᵇᵃᵇᵇᵘ웃ᵐᵉˡᵃ유‎ˢᵒⁿᵃ‎ ‎"
    elif 50 <= bikash < 60:
        bar = "🐒ᶜᵘᵍˡⁱ.🙊웃🙉유‎🙈"
    elif 60 <= bikash < 70:
        bar = " ‎ ‎ 웃⚔.ᶠⁱᵍʰᵗ.⚔유 ‎ "
    elif 70 <= bikash < 80:
        bar = "유ᵇʰᵃʳ ᵍʸᵃ ᵐⁿ🐕‍🦺..웃"
    elif 80 <= bikash < 95:
        bar = "유ᵇʳᵃᵏᵘᵖ... ↮ˢᵒʳʳʸ웃"
    else:
        bar = "유♡옻.ᵉⁿᵈ🍾+🚬=웃"
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text= " ➕ ", url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text="sᴋɪᴘ ᴛʜᴇ sᴏɴɢ—‣‣", callback_data=f"ADMIN Skip|{chat_id}")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text= " ➕ ", url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text="sᴋɪᴘ ᴛʜᴇ sᴏɴɢ—‣‣", callback_data=f"ADMIN Skip|{chat_id}")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
