from datetime import  datetime

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
        pass

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
