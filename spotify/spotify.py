import json
from pprint import pprint
from setup import api_setup

api = api_setup()

user_playlists = api.user_playlists('22cibcwsgccqgovymihtk5v7y')
album = api.album("10NuGMCidwcNSHZIJDBXPu")
#pprint(user_playlists)
#with open("result.json", "w+") as fp:
#    json.dump(user_playlists, fp)

#print(user_playlists["items"][0].keys())
#print(api._get(user_playlists["items"][0]["tracks"]["href"]))
playlist_tracks = api._get(user_playlists["items"][0]["tracks"]["href"])
with open("result.json", "w+") as fp:
    json.dump(album, fp, indent=4)

#id = user_playlists["items"][0]["owner"]["id"]


'''
user = api.user('22cibcwsgccqgovymihtk5v7y')
with open("result.json", "w+") as fp:
    json.dump(user, fp)
'''