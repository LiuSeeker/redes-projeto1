#https://api.spotify.com/v1/playlists/4LAe6LdE6xlKOW1KlESeaA/tracks

import json
from pprint import pprint
from setup import api_setup
import time
import datetime


def str_to_timestamp_parser(texto):
    texto = texto[0:10]
    return datetime.datetime.strptime(texto, "%Y-%m-%d").timestamp()


api = api_setup()


playlist_tracks = api._get("https://api.spotify.com/v1/playlists/4LAe6LdE6xlKOW1KlESeaA/tracks")

print("")
pprint(playlist_tracks["items"][0].keys())
pprint(playlist_tracks["items"][0]["added_by"])
#times = str_to_timestamp_parser(playlist_tracks["items"][0]["added_at"])
#print(times, type(times))
print("")