from datetime import datetime
import os
import csv

# Magic strings for the performance data map
NUM_OF_RECORDS = "num_of_records"
TIME_CONSUMED = "time_consumed"
START_TIME = "start_time"
END_TIME = "end_time"
MERGE_ALGORITHM = "merge_algorithm"


class DataSorter:

    def __init__(self):
        self.data = []
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.algorithm_used = ""

    # Exercise 25
    def set_input_data(self, file_path_name: str):
        if type(file_path_name) is not str:
            raise TypeError
        if not os.path.exists(file_path_name) and os.path.isfile(file_path_name):
            raise FileNotFoundError
        elif not file_path_name.lower().endswith(".csv"):
            raise NotCSVException
        else:
            self.data = []
            with open(file_path_name, newline= '') as csvfile:
                dialect = csv.Sniffer().sniff(csvfile.read(1024), [',','|'])
                csvfile.seek(0)
                items = csv.reader(csvfile,dialect)
                for row in items:
                    for i in row:
                        self.data.append(i)

            return True

    # Exercise 26
    def set_output_data(self, file_path_name: str):
        pass

    # Exercise 27
    def execute_merge_sort(self):
        # Remember to track the name of the algorithm in self.algorithm_used
        #  and to store the value of datetime.now() in self.start_time and
        #  self.end_time at appropriate times
        self.algorithm_used = "Merge Sort"

    # Exercise 30
    def get_performance_date(self) -> dict:
        return {
            NUM_OF_RECORDS: len(self.data),
            TIME_CONSUMED: self.end_time - self.start_time,
            START_TIME: self.start_time,
            END_TIME: self.end_time,
            MERGE_ALGORITHM: self.algorithm_used
        }


class NotCSVException(Exception):
    pass
