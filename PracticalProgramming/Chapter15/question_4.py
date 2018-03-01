import unittest


class TestSorting(unittest.TestCase):
    """ Test is_sorted """

    def test_is_sorted_empty(self):
        """ Test empty list """

        self.assertEqual(True, is_sorted([]))

    def test_is_sorted_single(self):
        """ Test single item """

        self.assertEqual(True, is_sorted([5]))

    def test_is_sorted_dups(self):
        """ Test list with duplicate values """

        self.assertEqual(True, is_sorted([1, 2, 3, 3, 5]))

    def test_is_sorted_desc(self):
        """ Test list descending order """

        self.assertEqual(False, is_sorted([5, 4, 3, 2]))

    def test_is_sorted_mixed(self):
        """ Test unsorted list """

        self.assertEqual(False, is_sorted([1, 5, 2, 4]))
