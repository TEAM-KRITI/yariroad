import json, os

import config

DEFAULT = {"mods": {}, "words": [], "msgdelete": None, "mediadelete": None}


class Database:
    """MongoDB if MONGO_URI is set, otherwise a local JSON file."""

    def __init__(self):
        self.cache = {}
        self.col = None
        if config.MONGO_URI:
            from pymongo import MongoClient
            self.col = MongoClient(config.MONGO_URI)[config.DB_NAME]["chats"]
        else:
            self.path = "data.json"
            if os.path.exists(self.path):
                with open(self.path) as f:
                    self.cache = {int(k): v for k, v in json.load(f).items()}

    def get(self, chat_id):
        if chat_id not in self.cache:
            doc = self.col.find_one({"_id": chat_id}) if self.col is not None else None
            base = json.loads(json.dumps(DEFAULT))
            if doc:
                base.update({k: v for k, v in doc.items() if k != "_id"})
            self.cache[chat_id] = base
        return self.cache[chat_id]

    def save(self, chat_id):
        doc = self.cache[chat_id]
        if self.col is not None:
            self.col.replace_one({"_id": chat_id}, {"_id": chat_id, **doc}, upsert=True)
        else:
            with open(self.path, "w") as f:
                json.dump({str(k): v for k, v in self.cache.items()}, f)


db = Database()
