import os


class Settings():
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_DATABASE_URI = ''


from local_settings import *