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

track = api.track("https://api.spotify.com/v1/track/4tmwiN9YU7xMjh2hoqcVuI")

print("")
pprint(track["name"])
print("")
#pprint(playlist_tracks["items"][0]["track"])

#track_features = api.audio_features(7HB2Waepqi7Ht68ZLKV2C0)
'''
with open("track.json", "w+") as fp:
    json.dump(track["items"][0]["track"], fp, indent=4)
'''
#times = str_to_timestamp_parser(playlist_tracks["items"][0]["added_at"])
#print(times, type(times))
print("")