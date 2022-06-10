import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate('firebase/service_account.json')


def initialize_firebase_app():
    firebase_admin.initialize_app(cred)

