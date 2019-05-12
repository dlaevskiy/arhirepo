import unittest
from math_parser_v1 import parse


class TestParcing(unittest.TestCase):

    def test1(self):
        L = []
        for el in parse('77====77'):
            L.append(el)
        self.assertEqual(L, ['77', '====', '77'])


if __name__ == '__main__':
    unittest.main()
