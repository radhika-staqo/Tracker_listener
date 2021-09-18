

def get_tracker_data_insert_query(data):
    imei = data.get("imei")
    tracker_data = data.get("tracker_data")
    ip_address = data.get("ip_address")
    return """
        INSERT INTO tracker_data (imei, tracker_data, ip_address) 
        VALUES (
        {}, "{}", "{}"
        )
    """.format(
        imei, tracker_data, ip_address
    )
