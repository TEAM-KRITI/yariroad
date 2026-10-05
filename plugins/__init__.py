from telegram.ext import CommandHandler, filters

from helpers import make_toggle
from plugins import (abuse, biomode, edit, echo as _echo, linkfilter, mediadelete, msgdelete,
                     nohashtags, nophone, nopromo, noforward, nostylish, purge as _purge)

# order = order in which filters run
FILTERS = [noforward, nohashtags, nophone, linkfilter, nopromo, nostylish, abuse, biomode]
TOGGLE_MODULES = FILTERS + [edit]
ALL = {m.NAME: m for m in TOGGLE_MODULES + [mediadelete, msgdelete, _echo, _purge]}


def register_all(app):
    from plugins import start, settings, guard, image
    start.register(app)
    for m in TOGGLE_MODULES:
        app.add_handler(CommandHandler(m.NAME, make_toggle(m.NAME), filters=filters.ChatType.GROUPS))
    for m in (abuse, mediadelete, msgdelete, _echo, _purge, settings, image):
        m.register(app)
    guard.register(app)  # last, catch-all message guard
