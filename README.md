# Meow Guard Bot

Telegram group security bot, one file per module.

```
bot.py            entry point
config.py         ALL settings (env vars, texts, tuning)
database.py       MongoDB / local JSON storage
helpers.py        admin check, warn, delete-later, toggle helpers
plugins/
  nohashtags.py  nopromo.py  nophone.py  noforward.py  nostylish.py
  biomode.py     linkfilter.py  abuse.py  edit.py          (filters)
  mediadelete.py msgdelete.py                               (timers)
  echo.py  purge.py  settings.py  start.py                  (commands/UI)
  guard.py         runs every enabled filter on each message
  __init__.py      plugin registry
```

## Add a new filter
Create `plugins/myfilter.py` with `NAME`, `HELP` and `async def check(context, msg, user, text, etypes)`
(return a reason string to delete, else None), then add it to `FILTERS` in `plugins/__init__.py`.

## Config (Heroku Config Vars)
`BOT_TOKEN` (required), `MONGO_URI` (recommended), `UPDATE_CHANNEL_URL`, `UPDATE_GROUP_URL`,
`WARN_DELETE_AFTER`, `ADMIN_CACHE_TTL`, `BIO_CACHE_TTL`, `STYLISH_MIN_CHARS`, `DEFAULT_BAD_WORDS`.

## Deploy on Heroku
1. Push repo to GitHub -> Heroku New App -> Deploy -> connect repo.
2. Settings -> Config Vars -> add `BOT_TOKEN` and `MONGO_URI`.
3. Deploy Branch, then Resources -> turn ON `worker` (turn `web` off).
CLI: `heroku config:set BOT_TOKEN=xxx MONGO_URI=xxx && git push heroku main && heroku ps:scale worker=1`

## Use
Add bot to group as admin (Delete messages). Admin commands: `/linkfilter on`, `/nopromo on`, `/abuse on`,
`/addabuse word`, `/mediadelete 30`, `/msgdelete 60`, `/echo text`, `/purge` (reply), `/settings`.
Admins are never filtered.

## Font & photo
- Every bot text uses the small-caps font (`fonts.py`). Set `FONT_STYLE=off` to disable.
- Photo on /start and help: set `OWNER_ID` (your Telegram id), then in the bot's PM send a photo with caption
  `/setimage` (or reply to a photo with `/setimage`). `/delimage` removes it. Or set `START_IMAGE` (URL/file_id).
