import re
from scripts.database_utility.db_query import *


def imei(n):
    if (len(n) == 15):
        return True
    else:
        return False


def get_data(msg_packet_2, address):
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
