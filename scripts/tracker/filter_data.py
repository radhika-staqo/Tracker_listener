from scripts.database_utility.db_query import *
import requests
import json
import re
from scripts.database_utility.db_query import insert_tracker_filtered_data


def post_data(tracker_data):
    data = {'device_imei_no': tracker_data.get("imei"), 'data': tracker_data.get("tracker_data")}
    data = json.dumps(data, indent=4)
    print(type(data))
    print(data)
    response = requests.post(url='http://34.234.229.50/api/user-tracking-logs', data=data)
    print(response.json)
    return response


def filter_tracker_data(tracker_data):
    """
                    --------------------------------------------
                    extract the data from the message receieved
    """
    status = post_data(tracker_data)
    insert_tracker_filtered_data(tracker_data, status)


def imei(n):
    """
                    --------------------------------
                    validates the device imei number
    """
    if (len(n) == 15):
        return True
    else:
        return False


def get_data(msg_packet_2, address):
    """
                    ------------------------------------------
                    gets the incoming message data separately
    """
    try:
        find_all_number = re.findall('[0-9]+', msg_packet_2)
        finalx = list(filter(imei, find_all_number))
        imei_number = finalx[0]
        data = {
            'imei': imei_number,
            'tracker_data': msg_packet_2.replace(imei_number, ''),
            'ip_address': address
        }
        print(data)
        insert_tracker_data(data)

    except Exception as e:
        print(e)
        print('TRACKER_DATA:', msg_packet_2)
