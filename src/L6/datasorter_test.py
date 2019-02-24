import os
import random
import unittest
from datetime import datetime

from L6.datasorter import DataSorter
from L6.datasorter import NotCSVException
from L6.datasorter import NUM_OF_RECORDS, ALGORITHM, MERGE_SORT, START_TIME, END_TIME, TIME_CONSUMED

# Magic Strings for filenames
TEST_FILE_1 = "test1.txt"
TEST_FILE_2 = "test2.csv"
TEST_FILE_3 = "test3.csv"


class DataSorterTest(unittest.TestCase):

    def setUp(self):
        self.under_test = DataSorter()

        with open(TEST_FILE_1, "w+") as file:
            file.write("1")

        with open(TEST_FILE_2, "w+") as file:
            file.write("1, 2, 3")

        with open(TEST_FILE_3, "w+") as file:
            file.write("q, p, t")

    def test_set_input_data_with_invalid_paths(self):
        with self.assertRaises(TypeError):
            self.under_test.set_input_data(48)
        with self.assertRaises(FileNotFoundError):
            self.under_test.set_input_data("test0.csv")

        with self.assertRaises(NotCSVException):
            self.under_test.set_input_data("test1.txt")

    def test_set_input_data_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.under_test.set_input_data("test3.csv")

    def test_set_input_data_with_valid_paths(self):
        self.assertTrue(self.under_test.set_input_data("test2.csv"))
        self.assertIsNotNone(self.under_test.data)
        self.assertIsInstance(self.under_test.data, list)
        self.assertEqual(3, len(self.under_test.data))
        self.assertEqual(3, self.under_test.data[2])

    def tearDown(self):

        for filename in TEST_FILE_1, TEST_FILE_2, TEST_FILE_3:
            if os.path.exists(filename):
                os.remove(filename)

    def test_merge_sort(self):
        # We'll test valid test cases here
        test_cases = [
            [],
            [3],
            [-1, -3, 5, 23, 2, 34, 5, 7],
            [0, 3, 2.3, 12, 5, 2.4, 2.39],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 2],
            # Random case with 50 int numbers
            [random.randint(1, 100) for _ in range(50)],
            # Random case with 30 float numbers
            [random.uniform(1, 100) for _ in range(30)]
        ]

        for case in test_cases:
            # Inject a simulation of the data
            self.under_test.data = case
            self.under_test.execute_merge_sort()
            result = self.under_test.data

            # All elements in the original list should be in the sorted list
            self.assertTrue(len(case) == len(result),
                            msg=f"The original list and the sorting list are not of the same size! "
                            f"Original: {len(case)} Sorted: {len(result)}")
            self.assertTrue(all([x in result for x in case]),
                            msg="Not all of the elements in the original list are in the sorted list!")

            # All values should be in ASC order
            self.assertTrue(all(result[i] <= result[i + 1] for i in range(len(result) - 1)),
                            msg=f"{case} was not sorted ASC using MergeSort, it showed as: {result}")

    def test_merge_sort_invalid_values(self):
        # We'll test invalid test cases here
        test_cases = [
            None,
            "This is not a list",
            [0, 3, 2, "5", 4],
            [9.3, 8, 7, 6, None, 0, -1, 2]
        ]

        for case in test_cases:
            # Inject a simulation of the data
            self.under_test.data = case

            with self.assertRaises(ValueError,
                                   msg=f"{case} was an invalid case but ValueError was not raised!"):
                self.under_test.execute_merge_sort()

    def test_get_performance_data(self):
        test_case = [random.randint(1, 100) for _ in range(100000)]
        self.under_test.data = test_case

        # Merge Sort
        expected_start_time = datetime.now()
        self.under_test.execute_merge_sort()
        expected_end_time = datetime.now()

        expected_time_executed = expected_end_time - expected_start_time
        expected_algorithm = MERGE_SORT

        result = self.under_test.get_performance_date()

        # We should get a non-none dict that is not empty
        self.assertIsNotNone(result)
        self.assertTrue(len(result) != 0)

        self.assertEqual(expected_algorithm, result[ALGORITHM])
        self.assertEqual(len(test_case), result[NUM_OF_RECORDS])

        # Let's give it a 16k-microsecond margin
        self.assertAlmostEqual(expected_start_time.microsecond, result[START_TIME].microsecond, delta=16000)
        self.assertAlmostEqual(expected_end_time.microsecond, result[END_TIME].microsecond, delta=16000)
        self.assertAlmostEqual(expected_time_executed.microseconds, result[TIME_CONSUMED].microseconds, delta=16000)
