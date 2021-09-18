

def get_tracker_data_insert_query(data):
    """
                ---------------------------------------------------
                insertion query for the incoming data from tracker
    """
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
    """
                 ------------------------------------------------
                 query to get the unfiltered data from the table
    """
    return """
        SELECT * FROM tracker_data WHERE parsed_status = "0"
    """


def get_tracker_filter_data_insert_query(data):
    """
                -----------------------------------------------------
                insertion query for the filtered data into the table
        """
    return """
        INSERT INTO <Table Name> (
        
        ) 
        VALUES (
        
        )
    """.format(

    )


def get_parsed_update_query(id):
    """
                    -------------------------------------
                    query for the parsed status updation
        """
    return """
        UPDATE tracker_data SET parsed_status = "1" WHERE id = "{}"
    """.format(id)
