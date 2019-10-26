import datetime
import json
import os
import time
from pprint import pprint

import pymysql
import requests
import urllib3

from setup import api_setup, mysql_setup

api = api_setup()

print(api.track("00p6D4NaakmWGNR3EUtxtS"))