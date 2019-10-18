from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import configparser
import json
import pymysql

def api_setup():
    config = configparser.ConfigParser()
    config.read("config.cfg")
    CLIENT_ID = config.get("SPOTIFY", "CLIENT_ID")
    CLIENT_SECRET = config.get("SPOTIFY", "CLIENT_SECRET")

    credential_manager = SpotifyClientCredentials(\
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    token = credential_manager.get_access_token()

    return Spotify(auth=token)

def mysql_setup():
    config = configparser.ConfigParser()
    config.read("config.cfg")
    HOST = config.get("MYSQL", "HOST")
    USER = config.get("MYSQL", "USER")
    PASSWORD = config.get("MYSQL", "PASSWORD")
    DATABASE = config.get("MYSQL", "DATABASE")

    connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE)

    return connection