import math

from pyrogram.types import InlineKeyboardButton

from LilyXMusic.utils.formatters import time_to_seconds


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
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "•ﮩـﮩﮩ٨ـsᴛᴀʀᴛﮩ٨ـﮩﮩ٨ـ"
    elif 10 < umm < 20:
        bar = "ﮩـﮩﮩ٨•ـʟɪʟʏﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= umm < 30:
        bar = "ﮩـﮩ•ﮩ٨ـᴛᴇᴀᴍﮩ٨ـﮩﮩ٨ـ"
    elif 30 <= umm < 40:
        bar = "ﮩـ•ﮩﮩ٨ـᴛʜᴜɴᴅᴇʀﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= umm < 50:
        bar = "ﮩـﮩﮩ٨ـ•ʙᴏᴛsﮩ٨ـﮩﮩ٨ـ"
    elif 50 <= umm < 60:
        bar = "ﮩـﮩﮩ٨ـᴛᴛʙ•ᴏᴘﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= umm < 70:
        bar = "ﮩـﮩﮩ٨ـɪsᴛᴋʜᴀʀ•ﮩ٨ـﮩﮩ٨ـ"
    elif 70 <= umm < 80:
        bar = "ﮩـﮩﮩ٨ـɴᴏᴏʀﮩ٨ـﮩﮩ•٨ـ"
    elif 80 <= umm < 95:
        bar = "ﮩـﮩﮩ٨ـᴋɪɴɢﮩ٨ـ•ﮩﮩ٨ـ"   
    else:
        bar = "ﮩـﮩﮩ٨ـᴇɴᴅﮩ٨ـﮩﮩ٨ـ•"
        
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝐈𝐈", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣𝐈𝐈", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
      [
            InlineKeyboardButton(
                text="🫧 ᴏᴡɴᴇꝛ 🫧", url="https://t.me/ll_ISTKHAR_BABY_lll",
            ),
            InlineKeyboardButton(
                text="🍬 sᴜᴘᴘᴏꝛᴛ 🍬", url="https://t.me/+pnDJxCG5VVphMTVl",
            )
        ],
         [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="𝐂ʟᴏsᴇ-𝐊ᴀʀᴏ")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝐈𝐈", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣𝐈", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
         ],
        [
            InlineKeyboardButton(
                text="🫧 ᴏᴡɴᴇꝛ 🫧", url="https://t.me/ll_ISTKHAR_BABY_lll",
            ),
            InlineKeyboardButton(
                text="🍬 sᴜᴘᴘᴏꝛᴛ 🍬", url="https://t.me/+pnDJxCG5VVphMTVl",
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="𝐂ʟᴏsᴇ-𝐊ᴀʀᴏ")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"VenomPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"VenomPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
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
       