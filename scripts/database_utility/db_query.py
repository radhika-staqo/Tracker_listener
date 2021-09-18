import os
from dotenv import load_dotenv, find_dotenv
from scripts.database_utility.connection import MysqlConnect
from scripts.database_utility.queries import *


def get_db_creds():
    load_dotenv(find_dotenv())
    db_creds = {
        "username": os.getenv("user"),
        "password": os.getenv("passwd"),
        "database": os.getenv("database"),
        "host": os.getenv("host"),
        "port": os.getenv("port")
    }
    return db_creds


def insert_tracker_data(data):
    db_creds = get_db_creds()
    sql_object = MysqlConnect(db_creds)
    db_connection = sql_object.connect()
    query = get_tracker_data_insert_query(data)
    status = sql_object.execute_insert(query)
    if status:
        print("Tracker Data Dumped.")
    else:
        print("Something went wrong !!!")
    db_connection.close()
