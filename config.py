"""All settings live here.
Values come from environment variables (Heroku Config Vars / .env).
"""

import os


# =========================================================
# REQUIRED
# =========================================================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")


# =========================================================
# DATABASE
# =========================================================

MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "kirti")


# =========================================================
# FONT / PHOTO
# =========================================================

# Available:
# "smallcaps" = ᴍᴀɴᴀɢᴇ style font
# "off"       = normal text
FONT_STYLE = os.getenv(
    "FONT_STYLE",
    "smallcaps"
)


# Telegram Owner ID
# /setimage command ke liye use hoga.
OWNER_ID = int(
    os.getenv("OWNER_ID", "0") or 0
)


# Start message image
# Image URL ya Telegram file_id dono use kar sakte ho.
START_IMAGE = os.getenv(
    "START_IMAGE",
    "https://files.catbox.moe/x5lytj.jpg"
)


# =========================================================
# /START BUTTONS
# =========================================================

UPDATE_CHANNEL_URL = os.getenv(
    "UPDATE_CHANNEL_URL",
    "https://t.me/kirti_bots"
)

UPDATE_GROUP_URL = os.getenv(
    "UPDATE_GROUP_URL",
    "https://t.me/kirti_bots_support"
)


# =========================================================
# BEHAVIOUR TUNING
# =========================================================

# Warning message kitne seconds baad delete hoga
WARN_DELETE_AFTER = int(
    os.getenv(
        "WARN_DELETE_AFTER",
        "5"
    )
)


# Admin check cache time
ADMIN_CACHE_TTL = int(
    os.getenv(
        "ADMIN_CACHE_TTL",
        "60"
    )
)


# User bio cache time
BIO_CACHE_TTL = int(
    os.getenv(
        "BIO_CACHE_TTL",
        "600"
    )
)


# Stylish characters trigger karne ke liye
# minimum characters
STYLISH_MIN_CHARS = int(
    os.getenv(
        "STYLISH_MIN_CHARS",
        "3"
    )
)


# =========================================================
# DEFAULT BAD WORDS
# =========================================================

DEFAULT_BAD_WORDS = [
    word.strip()
    for word in os.getenv(
        "DEFAULT_BAD_WORDS",
        "fuck,bitch,bastard,slut,asshole"
    ).split(",")
    if word.strip()
]


# =========================================================
# START MESSAGE
# =========================================================

START_TEXT = (
    "🛡 <b>ʜᴇʟʟᴏ {name}! 👋</b>\n\n"

    "🤖 <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ꜱᴇᴄᴜʀɪᴛʏ ʙᴏᴛ</b>\n"
    "ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ᴋᴇᴇᴘ ʏᴏᴜʀ ɢʀᴏᴜᴘ "
    "ᴄʟᴇᴀɴ, ꜱᴀꜰᴇ ᴀɴᴅ ᴘʀᴏᴛᴇᴄᴛᴇᴅ. 🛡️\n\n"

    "✨ <b>ꜰᴇᴀᴛᴜʀᴇꜱ</b>\n"
    "┣ 🗑 ᴜɴᴡᴀɴᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ᴅᴇʟᴇᴛɪᴏɴ\n"
    "┣ 🚫 ᴘʀᴏᴍᴏᴛɪᴏɴ & ʟɪɴᴋ ꜰɪʟᴛᴇʀ\n"
    "┣ 📵 ᴘʜᴏɴᴇ & ʜᴀꜱʜᴛᴀɢ ᴄᴏɴᴛʀᴏʟ\n"
    "┗ ⚡ ꜰᴀꜱᴛ ɢʀᴏᴜᴘ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ\n\n"

    "📣 <b>ꜱᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ</b>\n"
    "ᴛᴀᴘ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇ ʙᴜᴛᴛᴏɴꜱ "
    "ꜰᴏʀ ʟᴀᴛᴇꜱᴛ ɴᴇᴡꜱ. 🔔\n\n"

    "➕ <b>ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ</b>\n"
    "ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ "
    "<b>ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ</b> "
    "ᴘᴇʀᴍɪꜱꜱɪᴏɴ. 🛡️\n\n"

    "📚 <b>ɴᴇᴇᴅ ʜᴇʟᴘ?</b>\n"
    "ᴛᴀᴘ <b>ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ</b> "
    "ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ."
)


# =========================================================
# HELP MESSAGE
# =========================================================

HELP_TEXT = (
    "📚 <b>ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘ</b>\n\n"

    "ʜᴇʀᴇ ʏᴏᴜ'ʟʟ ꜰɪɴᴅ "
    "ᴅᴇᴛᴀɪʟꜱ ꜰᴏʀ ᴀʟʟ "
    "ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴜɢɪɴꜱ "
    "ᴀɴᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\n"

    "🛡 <b>ᴘʀᴏᴛᴇᴄᴛɪᴏɴ</b>\n"
    "ʙʟᴏᴄᴋ ᴜɴᴡᴀɴᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ "
    "ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ɢʀᴏᴜᴘ ꜱᴀꜰᴇ.\n\n"

    "👇 <b>ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ</b>\n"
    "ᴛᴏ ᴠɪᴇᴡ ʜᴇʟᴘ "
    "ꜰᴏʀ ᴇᴀᴄʜ ᴍᴏᴅᴜʟᴇ."
)
