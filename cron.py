from scripts.tracker.filter_data import filter_tracker_data
from scripts.database_utility.db_query import *


def dump_filter_tracker_date():
    unfiltered_data = get_tracker_unfiltered_data()
    for data in unfiltered_data:
        filter_tracker_data(data)


def run():
    dump_filter_tracker_date()


if __name__ == "__main__":
    run()