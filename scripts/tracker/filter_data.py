from scripts.database_utility.db_query import *
import re
from scripts.database_utility.db_query import insert_tracker_filtered_data


def filter_tracker_data(tracker_data):
    """
                    --------------------------------------------
                    extract the data from the message receieved
    """
    text = tracker_data.get("tracker_data")
    if "CMD-X" not in text:
        date = re.findall("DATE:\s*([\w-]+)", text)[0]
        time = re.findall("TIME:\s*([\w-]+)", text)[0]
        lat = re.findall("LAT:\s*([^\n,]+)", text)[0]
        lot = re.findall("LOT:\s*([^\n,]+)", text)[0]
        speed = re.findall("Speed:\s*([^\n,]+)", text)[0]
        tracker_dict = {
            'Device_imei_no': tracker_data.get("imei"),
            'Date': date,
            'Time': time,
            'Latitude': lat,
            'Longitude': lot,
            'Speed': speed
            }
        print(tracker_dict)
        insert_tracker_filtered_data(tracker_data, tracker_dict)
    else:
        print(text)


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
