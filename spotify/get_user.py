import json
from pprint import pprint
from setup import api_setup

def get_user(user_id):
    api = api_setup()

    user = api.user(user_id)

    del user["external_urls"]
    del user["href"]
    user["followers"] = user["followers"]["total"]
    del user["images"]
    del user["type"]
    del user["uri"]
    user["id_user"] = user.pop("id")

    return user