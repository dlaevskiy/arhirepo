import unittest

from math_parser_v1 import process_unary_operations


class TestProcessUnaryOperations(unittest.TestCase):

    def test1(self):
        list_ = process_unary_operations(['-', '-', 13.0, ])
        self.assertEqual(list_, [13.0])

    def test2(self):
        list_ = process_unary_operations(['-', '-', '-', 13.0, ])
        self.assertEqual(list_, ['-', 13.0])

    def test3(self):
        list_ = process_unary_operations(['-', '-', '-', '-', 13.0, ])
        self.assertEqual(list_, [13.0])

    def test4(self):
        list_ = process_unary_operations(['+', '-', '+', '+', 13.0, ])
        self.assertEqual(list_, ['-', 13.0])

    def test5(self):
        list_ = process_unary_operations(['-', '(', '-', 13.0, ')'])
        self.assertEqual(list_, ['-', '(', '-', 13.0, ')'])

    def test6(self):
        list_ = process_unary_operations(['-', '(', '-', '-', 13.0, ')'])
        self.assertEqual(list_, ['-', '(', 13.0, ')'])

    def test7(self):
        list_ = process_unary_operations(['+', '+', '+', '+', 13.0, ])
        self.assertEqual(list_, ['+', 13.0])

    def test8(self):
        list_ = process_unary_operations([1.0, '*', '-', '-', 13.0, ])
        self.assertEqual(list_, [1.0, '*', 13.0])

    def test9(self):
        list_ = process_unary_operations([1.0, '*', '-', 13.0, ])
        self.assertEqual(list_, [1.0, '*', '-', 13.0])

    def test10(self):
        list_ = process_unary_operations([1.0, '*', '+', 13.0, ])
        self.assertEqual(list_, [1.0, '*', 13.0])

    def test11(self):
        list_ = process_unary_operations([1.0, '*', '(', '+', 13.0, ')'])
        self.assertEqual(list_, [1.0, '*', '(', 13.0, ')'])

    def test12(self):
        list_ = process_unary_operations(['(', 1.0, '+', 13.0, ')'])
        self.assertEqual(list_, ['(', 1.0, '+', 13.0, ')'])
    
    def test13(self):
        list_ = process_unary_operations(['-', '-', '-', '-', '-', 1.0, '-', '+', '(', '-', 1.0, ')'])
        self.assertEqual(list_, ['-', 1.0, '-', '(', '-', 1.0, ')'])

    def test14(self):
        list_ = process_unary_operations(['-', '+', '-', '-', '-', '+', '-', 1.0])
        self.assertEqual(list_, ['-', 1.0])

    def test15(self):
        list_ = process_unary_operations(['-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', 1.0])
        self.assertEqual(list_, [1.0])

    def test16(self):
        list_ = process_unary_operations(['-', '+', '(', '-', '-', '+', '-', 1.0, ')'])
        self.assertEqual(list_, ['-', '(', '-', 1.0, ')'])

    def test17(self):
        list_ = process_unary_operations(['+', '+', '-', '-', '+', '+', '-', '(', '-', 1.0, ')'])
        self.assertEqual(list_, ['-', '(', '-', 1.0, ')'])

    def test18(self):
        list_ = process_unary_operations([1, '-', '-', '-', 1.0])
        self.assertEqual(list_, [1.0, '-', 1.0])

    def test19(self):
        list_ = process_unary_operations([1.0, '-', '-', 1.0, '-', '-', 1.0])
        self.assertEqual(list_, [1.0, '+', 1.0, '+', 1.0])

    def test20(self):
        list_ = process_unary_operations([1.0, '-', '+', 1.0, '+', '-', 1.0])
        self.assertEqual(list_, [1.0, '-', 1.0, '-', 1.0])

    def test21(self):
        list_ = process_unary_operations(['+', '+', '+', '+', '+', 1.0])
        self.assertEqual(list_, [1.0])

    def test22(self):
        list_ = process_unary_operations(['-', '-', '-', '-', '-', 1.0])
        self.assertEqual(list_, ['-', 1.0])

    def test23(self):
        list_ = process_unary_operations(['+', '+', '(', '+', '(', '+', '+', 1.0, ')', ')'])
        self.assertEqual(list_, ['(', '(', 1.0, ')', ')'])

    def test24(self):
        list_ = process_unary_operations(['-', '(', '-', '+', '(', '-', '+', 1.0, ')', ')'])
        self.assertEqual(list_, ['-', '(', '-', '(', '-', 1.0, ')', ')'])
