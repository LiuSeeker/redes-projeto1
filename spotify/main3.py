import datetime
import json
import os
import time
from pprint import pprint

import pymysql
import requests
import urllib3
import spotipy

from setup import api_setup, mysql_setup

api = api_setup()

conn = mysql_setup()

def track_loop(id_track):
    track = api.track(id_track)

    id_album = track["album"]["id"]
    id_track = track["id"]
 
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Album_Track (id_album, id_track) VALUES (%s, %s)",
                            (id_album, id_track))
        except pymysql.err.IntegrityError as e:
            print("Erro: não foi possivel dar adicionar a track em album: {}".format(e))
            pass

def errorPrint(error):
    print("\n\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
    print(error)
    print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !\n")

def main():
    print("")

    global api, conn
    with conn.cursor() as cursor:
        cursor.execute("SET autocommit=1")

    with conn.cursor() as cursor:
        cursor.execute("SELECT id_track FROM Track")
        tracks = cursor.fetchall()
    
    i = 0
    while i < len(tracks):
        try:
            track_loop(tracks[i][0])
            i += 1
        except (OSError, requests.exceptions.ConnectionError, urllib3.exceptions.ProtocolError) as e:
            errorPrint(e)
            print("Restantando o programa e a conexao do spotify\n")
            api = api_setup()
            continue
        except pymysql.err.OperationalError as e:
            errorPrint(e)
            print("Restantando o programa e a conexao do mysql\n")
            conn = mysql_setup()
            continue
        except TypeError as e:
            errorPrint(e)
            print("Restantando o programa\n ")
            continue
        except (spotipy.client.SpotifyException) as e:
            errorPrint(e)
            print("Restantando o programa e a conexao do spotify\n")
            api = api_setup()
            continue


if __name__ == '__main__':
    main()
