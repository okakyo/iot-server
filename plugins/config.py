# ここに、Config 関連についてのコードをまとめる

import os 
from os.path import join,dirname
from dotenv import load_dotenv
from firebase_admin import credentials

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__),".env")
firebaseKey = join(dirname(__file__),"accessKey.json")
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

FirebasePlugin =credentials.Certificate(firebaseKey)
