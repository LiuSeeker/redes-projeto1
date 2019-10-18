import json
from pprint import pprint
from setup import api_setup

api = api_setup()

artist = api._get("https://api.spotify.com/v1/genre/otacore")

#pprint(artist)

with open("artist.json", "w+") as fp:
    json.dump(artist, fp, indent=4)