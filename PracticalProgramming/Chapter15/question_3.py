import unittest


class TestPrefixes(unittest.TestCase):
    """ Test all_prefixes """

    def test_empty_string(self):
        """ Empty string test """

        expected = set()
        actual = all_prefixes("")
        self.assertEqual(expected, actual)

    def test_single_char(self):
        """ Test a single character string """

        expected = {'s'}
        actual = all_prefixes("s")
        self.assertEqual(expected, actual)

    def test_multi_char_string(self):
        """ Test a string """

        expected = {'r', 'ro', 'rob', 'robi', 'robin'}
        actual = all_prefixes("robin")
        self.assertEqual(expected, actual)

    def test_similar_chars(self):
        """ Similar occurences of first letter """

        expected = {'p', 'pu', 'pup', 'pupp', 'puppe', 'puppet', 'pp', 'ppe', 'ppet', 'pe', 'pet'}
        actual = all_prefixes("puppet")
        self.assertEqual(expected, actual)
