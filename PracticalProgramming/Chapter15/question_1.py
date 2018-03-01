import unittest
from code_samples import double_preceding


class TestDoublePreceding(unittest.TestCase):
    """ Tests for  double_preceding """

    def test_double_preceding_empty(self):
        """ Empty list """

        expected = []
        argument = []
        double_preceding(argument)
        self.assertEqual(expected, argument)

    def test_double_preceding_single(self):
        """ Single item in list """

        expected = [0]
        argument = [5]
        double_preceding(argument)
        self.assertEqual(expected, argument)

    def test_double_preceding_two_items(self):
        """ Two items in list """

        argument = [5, 2]
        expected = [0, 10]
        double_preceding(argument)
        self.assertEqual(expected, argument)

    def test_double_preceding_multi_items(self):
        """ Multiple items in list """

        argument = [2, 5, 7, 4, 9]
        expected = [0, 4, 10, 14, 8]
        double_preceding(argument)
        self.assertEqual(expected, argument)

    def test_double_preceding_first_zero(self):
        """ First item zero in list """

        argument = [0, 2, 3, 5]
        expected = [0, 0, 4, 6]
        double_preceding(argument)
        self.assertEqual(expected, argument)


unittest.main()
