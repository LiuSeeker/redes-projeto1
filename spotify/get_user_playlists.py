import json
from pprint import pprint
from setup import api_setup

#def get_user_playlists(user_id):
api = api_setup()

user_playlists = api.user_playlists("22cibcwsgccqgovymihtk5v7y")

for playlist in user_playlists["items"]:
    del playlist["external_urls"]
    del playlist["href"]
    #playlist["images"] = playlist["images"][0]["url"]
    #playlist["image"] = playlist.pop("images")
    playlist["owner"] = playlist["owner"]["id"]
    playlist["owner_id"] = playlist.pop("owner")
    del playlist["primary_color"]
    del playlist["snapshot_id"]
    playlist["playlist_name"] = playlist.pop("name")
    del playlist["type"]
    del playlist["uri"]

#pprint(user_playlists["items"][0])
with open("user_playlists.json", "w+") as fp:
    json.dump(user_playlists["items"][0], fp, indent=4)
    #return user_playlists