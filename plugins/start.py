import html

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import CallbackQueryHandler, CommandHandler

import config
from fonts import style
from helpers import get_image, log


# =========================================================
# HELP ORDER
# =========================================================

HELP_ORDER = [
    "nohashtags",
    "nopromo",
    "nophone",
    "noforward",
    "nostylish",
    "biomode",
    "linkfilter",
    "abuse",
    "echo",
    "edit",
    "mediadelete",
    "msgdelete",
]


# =========================================================
# HELP BUTTON LABELS
# =========================================================

LABELS = {
    "nohashtags": "ɴᴏ ʜᴀꜱʜᴛᴀɢꜱ",
    "nopromo": "ɴᴏ ᴘʀᴏᴍᴏ",
    "nophone": "ɴᴏ ᴘʜᴏɴᴇ",
    "noforward": "ɴᴏ ꜰᴏʀᴡᴀʀᴅ",
    "nostylish": "ɴᴏ ꜱᴛʏʟɪꜱʜ",
    "biomode": "ʙɪᴏ ᴍᴏᴅᴇ",
    "linkfilter": "ʟɪɴᴋ ꜰɪʟᴛᴇʀ",
    "abuse": "ᴀʙᴜꜱᴇ",
    "echo": "ᴇᴄʜᴏ",
    "edit": "ᴇᴅɪᴛ",
    "mediadelete": "ᴍᴇᴅɪᴀ ᴅᴇʟᴇᴛᴇ",
    "msgdelete": "ᴍᴇꜱꜱᴀɢᴇ ᴅᴇʟᴇᴛᴇ",
}


HTML = ParseMode.HTML


# =========================================================
# BUTTON
# =========================================================

def btn(label, **kwargs):
    """
    Create a Telegram inline button
    with the configured stylish font.
    """

    return InlineKeyboardButton(
        text=style(str(label)),
        **kwargs
    )


# =========================================================
# START TEXT
# =========================================================

def start_text(name):
    """
    Create styled start message.
    """

    safe_name = html.escape(
        name or "User"
    )

    return style(
        config.START_TEXT
    ).format(
        name=safe_name
    )


# =========================================================
# START KEYBOARD
# =========================================================

def start_kb(bot_username):

    return InlineKeyboardMarkup([
        [
            btn(
                "ᴜᴘᴅᴀᴛᴇ↗",
                url=config.UPDATE_CHANNEL_URL,
            ),
            btn(
                "ᴜᴘᴅᴀᴛᴇ ɢʀᴏᴜp",
                url=config.UPDATE_GROUP_URL,
            ),
        ],

        [
            btn(
                "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ",
                callback_data="help",
            ),
        ],

        [
            btn(
                "ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ +",
                url=(
                    f"https://t.me/{bot_username}"
                    "?startgroup=true"
                    "&admin=delete_messages+restrict_members"
                ),
            ),
        ],
    ])


# =========================================================
# HELP KEYBOARD
# =========================================================

def help_kb():

    buttons = []

    for module in HELP_ORDER:

        label = LABELS.get(module)

        if not label:
            label = module.replace(
                "_",
                " "
            )

        buttons.append(
            btn(
                label,
                callback_data=f"h:{module}",
            )
        )

    # Two buttons per row
    rows = [
        buttons[i:i + 2]
        for i in range(
            0,
            len(buttons),
            2
        )
    ]

    # Purge button
    rows.append([
        btn(
            "ᴘᴜʀɢᴇ",
            callback_data="h:purge",
        )
    ])

    # Back button
    rows.append([
        btn(
            "ʙᴀᴄᴋ",
            callback_data="start",
        )
    ])

    return InlineKeyboardMarkup(rows)


# =========================================================
# SEND PANEL
# =========================================================

async def send_panel(message, text, kb):
    """
    Send panel with bot image.
    If image sending fails, send text instead.
    """

    image = get_image()

    if image:

        try:

            return await message.reply_photo(
                photo=image,
                caption=text,
                parse_mode=HTML,
                reply_markup=kb,
            )

        except Exception as e:

            log.warning(
                "photo failed, sending text only: %s",
                e,
            )

    return await message.reply_text(
        text,
        parse_mode=HTML,
        reply_markup=kb,
    )


# =========================================================
# SHOW / EDIT PANEL
# =========================================================

async def show(query, text, kb):
    """
    Edit an existing photo caption
    or normal text message.
    """

    try:

        if query.message.photo:

            await query.edit_message_caption(
                caption=text,
                parse_mode=HTML,
                reply_markup=kb,
            )

        else:

            await query.edit_message_text(
                text=text,
                parse_mode=HTML,
                reply_markup=kb,
            )

    except Exception as e:

        log.warning(
            "edit failed: %s",
            e,
        )


# =========================================================
# /START
# =========================================================

async def start(update, context):

    # Start only works in private chat
    if update.effective_chat.type != "private":
        return

    name = (
        update.effective_user.first_name
        or "User"
    )

    await send_panel(
        update.message,
        start_text(name),
        start_kb(
            context.bot.username
        ),
    )


# =========================================================
# /HELP
# =========================================================

async def help_cmd(update, context):

    await send_panel(
        update.message,
        style(config.HELP_TEXT),
        help_kb(),
    )


# =========================================================
# CALLBACK BUTTONS
# =========================================================

async def buttons(update, context):

    import plugins

    query = update.callback_query

    await query.answer()

    data = query.data

    # -----------------------------------------------------
    # BACK TO START
    # -----------------------------------------------------

    if data == "start":

        await show(
            query,
            start_text(
                query.from_user.first_name
            ),
            start_kb(
                context.bot.username
            ),
        )

        return

    # -----------------------------------------------------
    # HELP MENU
    # -----------------------------------------------------

    if data == "help":

        await show(
            query,
            style(config.HELP_TEXT),
            help_kb(),
        )

        return

    # -----------------------------------------------------
    # MODULE HELP
    # -----------------------------------------------------

    if data.startswith("h:"):

        module_name = data[2:]

        module = plugins.ALL.get(
            module_name
        )

        if module:

            help_text = getattr(
                module,
                "HELP",
                "ʜᴇʟᴘ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ.",
            )

            await show(
                query,
                style(help_text),
                InlineKeyboardMarkup([
                    [
                        btn(
                            "ʙᴀᴄᴋ",
                            callback_data="help",
                        )
                    ]
                ]),
            )


# =========================================================
# REGISTER HANDLERS
# =========================================================

def register(app):

    # /start
    app.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )

    # /help
    app.add_handler(
        CommandHandler(
            "help",
            help_cmd,
        )
    )

    # Inline buttons
    app.add_handler(
        CallbackQueryHandler(
            buttons,
        )
    )
