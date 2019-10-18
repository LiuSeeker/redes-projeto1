import json
from pprint import pprint
from setup import api_setup

def get_genre(genre_list):
    global db
    for genre in genre_list:
        db("INSERT INTO Genre (genre_name) VALUES (%s)".format(genre))


def get_artist(artist_id):
    global db
    api = api_setup()

    artist = api.artist(artist_id)
    del artist["external_urls"]
    artist["followers"] = artist["followers"]["total"]
    get_genre(artist["genres"])
    #del artist["genres"]
    del artist["href"]
    del artist["images"]
    del artist["type"]
    del artist["uri"]
    name = artist["name"]
    popularity = artist["popularity"]
    followers = artist["followers"]

    db("INSERT INTO Artist (id_artist, artist_name, popularity, followers) "
        "VALUES (%s, %s, %s, %s)".format(artist_id, name, popularity, followers))
    
    for genre in artist["genres"]:
        db("INSERT INTO Genre_Artist (genre_name, id_artist) "
            "VALUES (%s, %s)".format(genre, artist_id))


#artist = get_artist("62GoYifV4njTdvS8lD2yYT")

#with open("artist.json", "w+") as fp:
#    json.dump(artist, fp, indent=4)