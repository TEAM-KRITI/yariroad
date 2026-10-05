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

# MongoDB optional hai.
# Agar MONGO_URI nahi diya gaya to local data.json use hoga.
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "kirti")


# =========================================================
# FONT / PHOTO
# =========================================================

# Available:
# "smallcaps" = ᴍᴀɴᴀɢᴇ style font
# "off"       = normal text
FONT_STYLE = os.getenv("FONT_STYLE", "smallcaps")

# Telegram Owner ID
# /setimage command ke liye use hoga.
OWNER_ID = int(os.getenv("OWNER_ID", "0") or 0)

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
    os.getenv("WARN_DELETE_AFTER", "5")
)

# Admin check cache time
ADMIN_CACHE_TTL = int(
    os.getenv("ADMIN_CACHE_TTL", "60")
)

# User bio cache time
BIO_CACHE_TTL = int(
    os.getenv("BIO_CACHE_TTL", "600")
)

# Stylish characters trigger karne ke liye minimum characters
STYLISH_MIN_CHARS = int(
    os.getenv("STYLISH_MIN_CHARS", "3")
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
    "🤖 ɪ'ᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ's "
    "<b>ꜱᴇᴄᴜʀɪᴛʏ ʙᴏᴛ</b>, "
    "ᴋᴇᴇᴘɪɴɢ ᴄʜᴀᴛꜱ ᴄʟᴇᴀɴ ᴀɴᴅ ꜱᴀꜰᴇ.\n\n"
    "📣 <b>ꜱᴛᴀʏ ɪɴꜰᴏʀᴍᴇᴅ</b> "
    "ᴡɪᴛʜ ɪɴꜱᴛᴀɴᴛ ᴀʟᴇʀᴛꜱ.\n"
    "✅ <b>ᴀᴅᴅ ᴍᴇ ɴᴏᴡ</b> "
    "ᴀɴᴅ ɪ'ʟʟ ꜱᴛᴀʀᴛ "
    "ᴘʀᴏᴛᴇᴄᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘ!\n\n"
    "<i>ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ "
    "'ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ' "
    "ᴘᴇʀᴍɪꜱꜱɪᴏɴ.</i>"
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
    "👇 <b>ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ</b> "
    "ᴛᴏ ᴠɪᴇᴡ ʜᴇʟᴘ "
    "ꜰᴏʀ ᴇᴀᴄʜ ᴍᴏᴅᴜʟᴇ."
)
