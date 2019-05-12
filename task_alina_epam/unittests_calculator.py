import unittest

from math_parser_v1 import parse


class TestParcing(unittest.TestCase):

    def test1(self):
        list_ = []
        for el in parse('77====77'):
            list_.append(el)
        self.assertEqual(list_, [77.0, '====', 77.0])

    def test2(self):
        list_ = []
        for el in parse('-13'):
            list_.append(el)
        self.assertEqual(list_, ['-', 13.0])

    def test3(self):
        list_ = []
        for el in parse('6-(-13)'):
            list_.append(el)
        self.assertEqual(list_, [6.0, '-', '(', '-', 13.0, ')'])

    def test4(self):
        list_ = []
        for el in parse('1+2*2'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', 2.0, '*', 2.0])

    def test5(self):
        list_ = []
        for el in parse('1+(2+3*2)*3'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', '(', 2.0, '+', 3.0, '*', 2.0, ')', '*', 3.0])

    def test6(self):
        list_ = []
        for el in parse('10*(2+1)'):
            list_.append(el)
        self.assertEqual(list_, [10.0, '*', '(', 2.0, '+', 1.0, ')'])

    def test7(self):
        list_ = []
        for el in parse('10^(2+1)'):
            list_.append(el)
        self.assertEqual(list_, [10.0, '^', '(', 2.0, '+', 1.0, ')'])

    def test8(self):
        list_ = []
        for el in parse('100/3^2'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 3.0, '^', 2.0])

    def test9(self):
        list_ = []
        for el in parse('100/3%2^2'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 3.0, '%', 2.0, '^', 2.0])

    def test10(self):
        list_ = []
        for el in parse('100/3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 3.0])

    def test11(self):
        list_ = []
        for el in parse('100=3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '=', 3.0])

    def test12(self):
        list_ = []
        for el in parse('100+3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '+', 3.0])

    def test13(self):
        list_ = []
        for el in parse('100//3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '//', 3.0])

    def test14(self):
        list_ = []
        for el in parse('pi+e'):
            list_.append(el)
        self.assertEqual(list_, ['pi', '+', 'e'])

    def test15(self):
        list_ = []
        for el in parse('sin(sin(1))'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'sin', '(', 1.0, ')', ')'])

    def test16(self):
        list_ = []
        for el in parse('sin(sin(1))+1+sin(1)'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'sin', '(', 1.0, ')', ')', '+', 1.0, '+', 'sin', '(', 1.0, ')'])

    def test17(self):
        list_ = []
        for el in parse('log(e)'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 'e', ')'])

    def test18(self):
        list_ = []
        for el in parse('sin(pi/2)'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'pi', '/', 2.0, ')'])

    def test19(self):
        list_ = []
        for el in parse('log10(100)'):
            list_.append(el)
        self.assertEqual(list_, ['log', 10.0, '(', 100.0, ')'])

    def test20(self):
        list_ = []
        for el in parse('sin(pi/2)*111*6'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'pi', '/', 2.0, ')', '*', 111.0, '*', 6.0])

    def test21(self):
        list_ = []
        for el in parse('2*sin(pi/2)'):
            list_.append(el)
        self.assertEqual(list_, [2.0, '*', 'sin', '(', 'pi', '/', 2.0, ')'])

    def test22(self):
        list_ = []
        for el in parse('abs(-5)'):
            list_.append(el)
        self.assertEqual(list_, ['abs', '(', '-', 5.0, ')'])

    def test23(self):
        list_ = []
        for el in parse('round(123.456789)'):
            list_.append(el)
        self.assertEqual(list_, ['round', '(', 123.456789, ')'])


if __name__ == '__main__':
    unittest.main()
