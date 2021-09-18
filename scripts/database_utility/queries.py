

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


def get_tracker_unfilter_data_insert_query():
    return """
        SELECT * FROM tracker_data WHERE parsed_status = "0"
    """


def get_tracker_filter_data_insert_query(data):
    return """
        INSERT INTO <Table Name> (
        
        ) 
        VALUES (
        
        )
    """.format(

    )


def get_parsed_update_query(id):
    return """
        UPDATE tracker_data SET parsed_status = "1" WHERE id = "{}"
    """.format(id)
