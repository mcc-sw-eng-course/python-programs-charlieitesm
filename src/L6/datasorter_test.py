import unittest
import os

from datasorter import DataSorter
from datasorter import NotCSVException


class DataSorterTest(unittest.TestCase):

    def setUp(self):
        self.under_test = DataSorter()
        file = open("test1.txt", "w+")
        file.write("1")
        file.close()
        file = open("test2.csv", "w+")
        file.write("1, 2, 3")
        file.close()

    def test_set_input_data_with_invalid_paths(self):
        with self.assertRaises(TypeError):
            self.under_test.set_input_data(48)
        with self.assertRaises(FileNotFoundError):
            self.under_test.set_input_data("test0.csv")

        with self.assertRaises(NotCSVException):
            self.under_test.set_input_data("test1.txt")

    def test_set_input_data_with_valid_paths(self):
        self.assertTrue(self.under_test.set_input_data("test2.csv"))
        self.assertIsNotNone(self.under_test.data)
        self.assertIsInstance(self.under_test.data, list)
        self.assertEqual(3, len(self.under_test.data))
        self.assertEqual('3', self.under_test.data[2])

    def tearDown(self):
        if os.path.exists("test1.txt"):
            os.remove("test1.txt")
        if os.path.exists("test2.csv"):
            os.remove("test2.csv")
