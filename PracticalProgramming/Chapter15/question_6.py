import unittest
from code_samples import average


class TestAverage(unittest.TestCase):
    """ Test cases for average """

    def test_average_empty(self):
        """ Test empty list """

        self.assertEqual(0.0, average([]))

    def test_average_single(self):
        """ Test single item """

        self.assertEqual(5.0, average([5]))

    def test_average_single_none(self):
        """ Test single item none """

        self.assertEqual(0.0, average([None]))

    def test_average_two_with_none(self):
        """ Test two items where one of the items is None """

        self.assertEqual(7.5, average([7.5, None]))

    def test_average_multi_nums(self):
        """ Test multiple items with all numbers """

        self.assertEqual(15.0, average([15, 26, 32, -13]))


unittest.main()
