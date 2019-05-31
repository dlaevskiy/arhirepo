import unittest

from task_alina_epam.math_parser_v1 import calc


class TestSorting(unittest.TestCase):
    # TODO: AssertionError: 11 != 11.11111111111111
    def test9(self):
        self.assertEqual(100 / 3 ** 2, calc([100.0, 3.0, 2.0, '^', '/']))
