import math
import unittest

from calc_draft import calc


class TestSorting(unittest.TestCase):
    # # TODO: TypeError: cannot concatenate 'str' and 'float' objects
    # def test34(self):
    #     expected_result = math.sin(math.pi/2.0**1.0) + math.log(1*4+2**2+1, 3**2)
    #     calc_result = calc(['pi', 2.0, 1.0, '^', '/', 'sin', 1.0, 4.0, '*', 2.0, 2.0, '^', '+',
    #                         1.0, '+', ',', 3.0, 2.0, '^', 'log', '+'])
    #     self.assertEqual(expected_result, calc_result)

    # logarithms
    # TODO: AssertionError: 3.0 != 8.0
    def test61(self):
        self.assertEqual(math.log(8.0, 2.0), calc([8.0, 2.0, 'log']))
