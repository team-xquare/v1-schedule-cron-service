import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    DB_URL = os.environ['MYSQL_URL']
    KEY = os.environ['KEY']
