import json
from pprint import pprint
from setup import api_setup
import time
import datetime

def str_to_timestamp_parser(texto):
    texto = texto[0:10]
    return datetime.datetime.strptime(texto, "%Y-%m-%d").timestamp()


api = api_setup()

album_tracks = api.album_tracks("10NuGMCidwcNSHZIJDBXPu")

print("")
#pprint(album_tracks["items"])
print("")
#pprint(playlist_tracks["items"][0]["track"])

#track_features = api.audio_features(7HB2Waepqi7Ht68ZLKV2C0)

with open("album_tracks.json", "w+") as fp:
    json.dump(album_tracks["items"], fp, indent=4)

#times = str_to_timestamp_parser(playlist_tracks["items"][0]["added_at"])
#print(times, type(times))
print("")