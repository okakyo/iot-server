# ここに、Config 関連についてのコードをまとめる

import os 
from os.path import join,dirname
from dotenv import load_dotenv
from firebase_admin import credentials

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__),".env")

load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
FIREBASE_TYPE=os.environ.get("type")
FIREBASE_PROJECT_ID=os.environ.get("project_id")
FIREBASE_PRIVATE_ID=os.environ.get("private_key_id")
FIREBASE_PRIVATE_KEY=os.environ.get("private_key")
FIREBASE_CLIENT_EMAIL=os.environ.get("client_email")
FIREBASE_CLIENT_ID=os.environ.get('client_id')
FIREBASE_AUTH_URI=os.environ.get("auth_uri")
FIREBASE_TOKEN_URI=os.environ.get('token_uri')
FIREBASE_AUTH_PROVIDER_X509_CERT_URL=os.environ.get("auth_provider_x509_cert_url")
FIREBASE_CLIENT_X509_CERT_URL=os.environ.get("client_x509_cert_url")

FirebasePlugin = credentials.Certificate({
    "type":FIREBASE_TYPE,
    "project_id":FIREBASE_PROJECT_ID,
    "private_key_id":FIREBASE_PRIVATE_ID,
    "private_key":FIREBASE_PRIVATE_KEY,
    "client_email":FIREBASE_CLIENT_EMAIL,
    "client_id":FIREBASE_CLIENT_ID,
    "auth_uri":FIREBASE_AUTH_URI,
    "token_uri":FIREBASE_TOKEN_URI,
    "auth_provider_x509_cert_url":FIREBASE_AUTH_PROVIDER_X509_CERT_URL,
    "client_x509_cert_url":FIREBASE_CLIENT_X509_CERT_URL
})
