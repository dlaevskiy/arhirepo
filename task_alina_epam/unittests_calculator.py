import unittest
import math

from math_parser_v1 import parse



class TestParcing(unittest.TestCase):

    def test1(self):
        list_ = []
        for el in parse('77====77'):
            list_.append(el)
        self.assertEqual(list_, [77.0, '====', 77.0])

    # def test1(self):
    #     list_ = []
    #     for el in parse('-13'):
    #         list_.append(el)
    #     self.assertEqual(list_, ['-', 13.0])
    #
    # def test1(self):
    #     list_ = []
    #     for el in parse('6-(-13)'):
    #         list_.append(el)
    #     self.assertEqual(list_, [6.0, '-', '(', '-', 13.0, ')'])

    def test2(self):
        list_ = []
        for el in parse('1+2*2'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', 2.0, '*', 2.0])

    def test3(self):
        list_ = []
        for el in parse('1+(2+3*2)*3'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', '(', 2.0, '+', 3.0, '*', 2.0, ')', '*', 3.0])

    def test4(self):
        list_ = []
        for el in parse('10*(2+1)'):
            list_.append(el)
        self.assertEqual(list_, [10.0, '*', '(', 2.0, '+', 1.0, ')'])

    def test5(self):
        list_ = []
        for el in parse('10^(2+1)'):
            list_.append(el)
        self.assertEqual(list_, [10.0, '^', '(', 2.0, '+', 1.0, ')'])

    def test6(self):
        list_ = []
        for el in parse('100/3^2'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 3.0, '^', 2.0])

    def test7(self):
        list_ = []
        for el in parse('100/3%2^2'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 3.0, '%', 2.0, '^', 2.0])

    def test8(self):
        list_ = []
        for el in parse('pi+e'):
            list_.append(el)
        self.assertEqual(list_, [math.pi, '+', math.e])

    def test9(self):
        list_ = []
        for el in parse('sin(sin(1))'):
            list_.append(el)
        self.assertEqual(list_, ['sin(sin(1))'])

    def test10(self):
        list_ = []
        for el in parse('sin(sin(1))+1+sin(1)'):
            list_.append(el)
        self.assertEqual(list_, ['sin(sin(1))', '+', 1.0, '+', 'sin(1)'])


if __name__ == '__main__':
    unittest.main()
