import json
from pprint import pprint
from setup import api_setup, mysql_setup
import time
import datetime
import pymysql

genres = ["rock", "pop", "jazz", "classic", "hip hop"]
api = api_setup()

for st in genres:
    print("\n\nPLAYLISTS DE: " + st + "------------------------------------------------------------------------")
    search_str = st
    result = api.search(search_str, type="playlist", limit=50)
    for i in result["playlists"]["items"]:
        
        print(i["name"])#, i["id"])