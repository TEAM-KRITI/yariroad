import html

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import CallbackQueryHandler, CommandHandler

import config
from fonts import style
from helpers import get_image, log

HELP_ORDER = ["nohashtags", "nopromo", "nophone", "noforward", "nostylish", "biomode",
              "linkfilter", "abuse", "echo", "edit", "mediadelete", "msgdelete"]
LABELS = {"nohashtags": "# NOHASHTAGS"}
HTML = ParseMode.HTML


def btn(label, **kw):
    return InlineKeyboardButton(style(label), **kw)


def start_text(name):
    return style(config.START_TEXT).format(name=html.escape(name))


def start_kb(bot_username):
    return InlineKeyboardMarkup([
        [btn("UPDATE CHANNEL ↗", url=config.UPDATE_CHANNEL_URL),
         btn("UPDATE GROUP ↗", url=config.UPDATE_GROUP_URL)],
        [btn("HELP & COMMANDS", callback_data="help")],
        [btn("ADD ME TO YOUR GROUP +",
             url=f"https://t.me/{bot_username}?startgroup=true&admin=delete_messages+restrict_members")],
    ])


def help_kb():
    btns = [btn(LABELS.get(n, n.upper()), callback_data=f"h:{n}") for n in HELP_ORDER]
    rows = [btns[i:i + 2] for i in range(0, len(btns), 2)]
    rows.append([btn("PURGE", callback_data="h:purge")])
    rows.append([btn("BACK", callback_data="start")])
    return InlineKeyboardMarkup(rows)


async def send_panel(message, text, kb):
    """Send text with the bot photo on top (if one is set)."""
    img = get_image()
    if img:
        try:
            return await message.reply_photo(img, caption=text, parse_mode=HTML, reply_markup=kb)
        except Exception as e:
            log.warning("photo failed, sending text only: %s", e)
    return await message.reply_text(text, parse_mode=HTML, reply_markup=kb)


async def show(q, text, kb):
    """Edit the panel in place (caption if it has a photo, text otherwise)."""
    try:
        if q.message.photo:
            await q.edit_message_caption(caption=text, parse_mode=HTML, reply_markup=kb)
        else:
            await q.edit_message_text(text, parse_mode=HTML, reply_markup=kb)
    except Exception as e:
        log.warning("edit failed: %s", e)


async def start(update, context):
    if update.effective_chat.type != "private":
        return
    await send_panel(update.message, start_text(update.effective_user.first_name), start_kb(context.bot.username))


async def help_cmd(update, context):
    await send_panel(update.message, style(config.HELP_TEXT), help_kb())


async def buttons(update, context):
    import plugins
    q = update.callback_query
    await q.answer()
    d = q.data
    if d == "start":
        await show(q, start_text(q.from_user.first_name), start_kb(context.bot.username))
    elif d == "help":
        await show(q, style(config.HELP_TEXT), help_kb())
    elif d.startswith("h:"):
        mod = plugins.ALL.get(d[2:])
        if mod:
            await show(q, style(mod.HELP), InlineKeyboardMarkup([[btn("BACK", callback_data="help")]]))


def register(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CallbackQueryHandler(buttons))
