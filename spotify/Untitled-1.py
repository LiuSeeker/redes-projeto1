import json
from pprint import pprint
from setup import api_setup
import pymysql
from functools import partial

def run_db_query(connection, query, args=None):
    with connection.cursor() as cursor:
        print('Executando query:')
        cursor.execute(query, args)
        for result in cursor:
            print(result)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1234567890',
    database='emprestimos')

db = partial(run_db_query, connection)



connection.close()