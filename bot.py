import logging

from telegram import Update
from telegram.ext import Application

import config
import plugins

logging.basicConfig(level=logging.INFO)


def main():
    if not config.BOT_TOKEN:
        raise SystemExit("BOT_TOKEN is not set (Heroku Config Vars or .env)")
    app = Application.builder().token(config.BOT_TOKEN).build()
    plugins.register_all(app)
    logging.info("Bot started")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()
