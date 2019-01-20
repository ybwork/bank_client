import os


class Settings():
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2://user:pass@host:port/db_name'


from local_settings import *