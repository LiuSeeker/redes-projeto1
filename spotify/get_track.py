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

#track = api.track("https://api.spotify.com/v1/track/4tmwiN9YU7xMjh2hoqcVuI")
search = api.search("top 50s", limit=50)
print("")
#pprint(track["album"])
print("")
#pprint(playlist_tracks["items"][0]["track"])

#track_features = api.audio_features(7HB2Waepqi7Ht68ZLKV2C0)

nexte = api._get(search["tracks"]["next"])
next2 = api._get(nexte["tracks"]["next"])
next3 = api._get(next2["tracks"]["next"])
next4 = api._get(next3["tracks"]["next"])

with open("nexte.json", "w+") as fp:
    json.dump(next4, fp, indent=4)
#times = str_to_timestamp_parser(playlist_tracks["items"][0]["added_at"])
#print(times, type(times))
print("")