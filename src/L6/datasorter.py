from datetime import datetime

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

    @staticmethod
    def validate_input_list(input_list: list):
        """
        Validates if input_list is not None and is a list of only int or floats, if the validation doesn't pass
        a ValueError will be raised
        :param input_list: a list of values to validate
        :raises: a ValueError if the validation fails
        """
        if list is None or type(input_list) is not list:
            raise ValueError("The input_list was either None or not a list at all!")

        # Check that all elements are either float or int
        if not all([type(x) is int or type(x) is float for x in input_list]):
            raise ValueError("The input_list contains values that are not int nor float!")

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
