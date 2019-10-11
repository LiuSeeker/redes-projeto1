import json
from pprint import pprint
from setup import api_setup

def get_user_playlists(user_id):
    api = api_setup()

    user_playlists = api.user_playlists(user_id)

    for playlist in user_playlists["items"]:
        del playlist["external_urls"]
        del playlist["href"]
        playlist["images"] = playlist["images"][0]["url"]
        playlist["owner"] = playlist["owner"]["id"]
        playlist["owner_id"] = playlist.pop("owner")
        playlist["image"] = playlist.pop("images")
        del playlist["primary_color"]
        del playlist["snapshot_id"]
        playlist["playlist_name"] = playlist.pop("name")
        del playlist["type"]
        del playlist["uri"]
        playlist["id_playlist"] = playlist.pop("id")

    return 