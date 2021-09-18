import os
from dotenv import load_dotenv, find_dotenv
from scripts.database_utility.connection import MysqlConnect
from scripts.database_utility.queries import *


def get_db_creds():
    """
                ----------------------------------------
                get credentials for database from dotenv
    """
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
    """
                 -------------------------------------------------
                 inserts the incoming data into the database table
    """
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


def insert_tracker_filtered_data(tracker_data, tracker_dict):
    """
                     -------------------------------------------------------------------------
                     inserts the filtered data from tracker dictionary into the database table
    """
    db_creds = get_db_creds()
    sql_object = MysqlConnect(db_creds)
    db_connection = sql_object.connect()
    query = get_tracker_filter_data_insert_query(tracker_dict)
    status = sql_object.execute_insert(query)
    if status:
        update_query = get_parsed_update_query(tracker_data.get("id"))
        sql_object.execute_insert(update_query)
    else:
        print("Something went wrong !!!")
    db_connection.close()


def get_tracker_unfiltered_data():
    """
                    --------------------------------------------------
                    insers the unfiltered data into the database table
    """
    db_creds = get_db_creds()
    sql_object = MysqlConnect(db_creds)
    db_connection = sql_object.connect()
    query = get_tracker_unfilter_data_insert_query()
    data = sql_object.execute_query(query)
    db_connection.close()
    return data