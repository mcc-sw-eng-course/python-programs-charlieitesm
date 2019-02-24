import random
import unittest

from L6.datasorter import DataSorter


class DataSorterTest(unittest.TestCase):

    def setUp(self):
        self.under_test = DataSorter()

    def tearDown(self):
        pass

    def test_merge_sort(self):
        # We'll test valid test cases here
        test_cases = [
            [],
            [3],
            [-1, -3, 5, 23, 2, 34, 5, 7],
            [0, 3, 2.3, 12, 5, 2.4, 2.39],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 2],
            # Random case with 50 numbers
            [random.randint(1, 100) for _ in range(50)]
        ]

        for case in test_cases:
            # Inject a simulation of the data
            self.under_test.data = case
            self.under_test.execute_merge_sort()
            result = self.under_test.data

            # The result list should be a new object list
            self.assertTrue(case is not result,
                            msg="The resulting sorted list is not a different object from the original unsorted list!")

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
