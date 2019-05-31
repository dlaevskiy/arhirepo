import math
import unittest

from task_alina_epam.math_parser_v1 import calc


class TestSorting(unittest.TestCase):
    def test12(self):
        self.assertEqual(math.log(math.e), calc([1.0, 2.0, '+']))
