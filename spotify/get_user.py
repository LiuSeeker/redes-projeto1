import json
from pprint import pprint
from setup import api_setup

#def get_user(user_id):
api = api_setup()

user = api.user("22cibcwsgccqgovymihtk5v7y")

del user["external_urls"]
del user["href"]
user["followers"] = user["followers"]["total"]
del user["images"]
del user["type"]
del user["uri"]

with open("user.json", "w+") as fp:
    json.dump(user, fp, indent=4)

    #return user