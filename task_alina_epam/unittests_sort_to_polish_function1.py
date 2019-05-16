import unittest

from math_parser_v1 import sort_to_polish


class TestSorting(unittest.TestCase):

    # Unary operators
    def test1(self):
        list_ = []
        for el in sort_to_polish(['-', 13.0]):
            list_.append(el)
        self.assertEqual(list_, [0.0, 13.0, '-'])

    def test2(self):
        list_ = []
        for el in sort_to_polish([6.0, '-', '(', '-', 13.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [6.0, 0.0, 13.0, '-', '-'])

    def test3(self):
        list_ = []
        for el in sort_to_polish([1.0, '-', 1.0]):
            list_.append(el)
        self.assertEqual(list_, [1.0, 1.0, '-'])

    def test4(self):
        list_ = []
        for el in sort_to_polish(['-', 1.0]):
            list_.append(el)
        self.assertEqual(list_, [0.0, 1.0, '-'])

    # Operation priority
    def test5(self):
        list_ = []
        for el in sort_to_polish([1.0, '+', 2.0, '*', 2.0]):
            list_.append(el)
        self.assertEqual(list_, [1.0, 2.0, 2.0, '*', '+'])

    def test6(self):
        list_ = []
        for el in sort_to_polish([1.0, '+', '(', 2.0, '+', 3.0, '*', 2.0, ')', '*', 3.0]):
            list_.append(el)
        self.assertEqual(list_, [1.0, 2.0, 3.0, 2.0, '*', '+', 3.0, '*', '+'])

    def test7(self):
        list_ = []
        for el in sort_to_polish([10.0, '*', '(', 2.0, '+', 1.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [10.0, 2.0, 1.0, '+', '*'])

    def test8(self):
        list_ = []
        for el in sort_to_polish([10.0, '^', '(', 2.0, '+', 1.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [10.0, 2.0, 1.0, '+', '^'])

    def test9(self):
        list_ = []
        for el in sort_to_polish([100.0, '/', 3.0, '^', 2.0]):
            list_.append(el)
        self.assertEqual(list_, [100.0, 3.0, 2.0, '^', '/'])

    def test10(self):
        list_ = []
        for el in sort_to_polish([100.0, '/', 3.0, '%', 2.0, '^', 2.0]):
            list_.append(el)
        self.assertEqual(list_, [100.0, 3.0, '/', 2.0, 2.0, '^', '%'])

    # Functions and constants
    def test11(self):
        list_ = []
        for el in sort_to_polish(['pi', '+', 'e']):
            list_.append(el)
        self.assertEqual(list_, ['pi', 'e', '+'])

    def test12(self):
        list_ = []
        for el in sort_to_polish(['log', '(', 'e', ')']):
            list_.append(el)
        self.assertEqual(list_, ['e', 'log'])

    def test13(self):
        list_ = []
        for el in sort_to_polish(['sin', '(', 'pi', '/', 2.0, ')']):
            list_.append(el)
        self.assertEqual(list_, ['pi', 2.0, '/', 'sin'])

    def test14(self):
        list_ = []
        for el in sort_to_polish(['log10', '(', 100.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [100.0, 'log10'])

    def test15(self):
        list_ = []
        for el in sort_to_polish(['sin', '(', 'pi', '/', 2.0, ')', '*', 111.0, '*', 6.0]):
            list_.append(el)
        self.assertEqual(list_, ['pi', 2.0, '/', 'sin', 111.0, '*', 6.0, '*'])

    def test16(self):
        list_ = []
        for el in sort_to_polish([2.0, '*', 'sin', '(', 'pi', '/', 2.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [2.0, 'pi', 2.0, '/', 'sin', '*'])

    def test17(self):
        list_ = []
        for el in sort_to_polish(['abs', '(', '-', 5.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [0.0, 5.0, '-', 'abs'])

    def test18(self):
        list_ = []
        for el in sort_to_polish(['round', '(', 123.456789, ')']):
            list_.append(el)
        self.assertEqual(list_, [123.456789, 'round'])

    # Associative
    def test19(self):
        list_ = []
        for el in sort_to_polish([102.0, '%', 12.0, '%', 7.0]):
            list_.append(el)
        self.assertEqual(list_, [102.0,  12.0, '%', 7.0, '%'])

    def test20(self):
        list_ = []
        for el in sort_to_polish([100.0, '/', 4.0, '/', 3.0]):
            list_.append(el)
        self.assertEqual(list_, [100.0,  4.0, '/', 3.0, '/'])

    def test21(self):
        list_ = []
        for el in sort_to_polish([2.0, '^', 3.0, '^', 4.0]):
            list_.append(el)
        self.assertEqual(list_, [2.0, 3.0, 4.0, '^', '^'])

    # Comparison operators
    def test22(self):
        list_ = []
        for el in sort_to_polish([1.0, '+', 2.0, '*', 3.0, '==', 1.0, '+', 2.0, '*', 3.0]):
            list_.append(el)
        self.assertEqual(list_, [1.0, 2.0, 3.0, '*', '+', 1.0, 2.0, 3.0, '*', '+', '=='])

    def test23(self):
        list_ = []
        for el in sort_to_polish(['e', '^', 5.0, '>=', 'e', '^', 5.0, '+', 1.0]):
            list_.append(el)
        self.assertEqual(list_, ['e', 5.0, '^', 'e', 5.0, '^', 1.0, '+', '>='])

    def test24(self):
        list_ = []
        for el in sort_to_polish([1.0, '+', 2.0, '*', 4.0, '/', 3.0, '+', 1.0, '!=',
                                  1.0, '+', 2.0, '*', 4.0, '/', 3.0, '+', 2.0]):
            list_.append(el)
        self.assertEqual(list_, [1.0, 2.0, 4.0, '*', 3.0, '/', '+', 1.0, '+', 1.0,
                                 2.0, 4.0, '*', 3.0, '/', '+', 2.0, '+', '!='])

    # Common tests
    def test25(self):
        list_ = []
        for el in sort_to_polish(['(', 100.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [100.0])

    def test26(self):
        list_ = []
        for el in sort_to_polish([666.0]):
            list_.append(el)
        self.assertEqual(list_, [666.0])

    def test27(self):
        list_ = []
        for el in sort_to_polish(['-', 0.1]):
            list_.append(el)
        self.assertEqual(list_, [0.1, '-'])

    def test28(self):
        list_ = []
        for el in sort_to_polish([1.0, '/', 3.0]):
            list_.append(el)
        self.assertEqual(list_, [1.0, 3.0, '/'])

    def test29(self):
        list_ = []
        for el in sort_to_polish([1.0, '/', 3.0]):
            list_.append(el)
        self.assertEqual(list_, [1.0, 3.0, '/'])

    def test30(self):
        list_ = []
        for el in sort_to_polish([0.1, '*', 2.0, '^', 56.0]):
            list_.append(el)
        self.assertEqual(list_, [0.1, 2.0, 56.0, '^',  '*'])

    def test31(self):
        list_ = []
        for el in sort_to_polish(['e', '^', 34.0]):
            list_.append(el)
        self.assertEqual(list_, ['e', 34.0, '^'])

    def test32(self):
        list_ = []
        for el in sort_to_polish(['(', 2.0, '^', '(', 'pi', '/', 'pi', '+', 'e', '/', 'e',
                                  '+', 2.0, '^', 0.0, ')', ')']):
            list_.append(el)
        self.assertEqual(list_, [2.0, 'pi', 'pi', '/', 'e', 'e', '/', '+', 2.0, 0.0, '^', '+', '^'])

    def test33(self):
        list_ = []
        for el in sort_to_polish(['(', 2.0, '^', '(', 'pi', '/', 'pi', '+', 'e', '/', 'e', '+', 2.0, '^', 0.0, ')',
                                  ')', '^', '(', 1.0, '/', 3.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [2.0, 'pi', 'pi', '/', 'e', 'e', '/', '+', 2.0, 0.0, '^', '+',
                                 '^', 1.0, 3.0, '/', '^'])

    def test34(self):
        list_ = []
        for el in sort_to_polish(['sin', '(', 'pi', '/', 2.0, '^', 1.0, ')', '+', 'log', '(', 1.0, '*', 4.0,
                                  '+', 2.0, '^', 2.0, '+', 1.0, ',', 3.0, '^', 2.0, ')']):
            list_.append(el)
        self.assertEqual(list_, ['sin', 'pi', '/', 2.0, 1.0, '^', '/', 'log', 1.0, 4.0, '*', 2.0, 2.0, '^', '+',
                                 1.0, '+', ',', 3.0, 2.0, '^', '+'])

    def test35(self):
        list_ = []
        for el in sort_to_polish([10.0, '*', 'e', '^', 0.0, '*', 'log10', '(', 0.4, '-', 5.0, '/', '-', 0.1, '-',
                                  10.0, ')', '+', 'abs', '(', '-', 53.0, '/', 10.0, ')', '-', 5.0]):
            list_.append(el)
        self.assertEqual(list_, [10.0, 'e', 0.0, '^', '*', 0.4, 5.0, '/', '-', 0.1, '-', 10.0, '-', 'log10', '*',
                                  53.0, 10.0, '/', '-', 'abs', '+', 5.0, '-'])

    def test36(self):
        list_ = []
        for el in sort_to_polish(['sin', '(', '-', 'cos', '(', '-', 'sin', '(', 3.0, ')', '-', 'cos',
                                  '(', '-', 'sin', '(', '-', 3.0, '*', 5.0, ')', '-', 'sin', '(', 'cos',
                                  '(', 'log10', '(', 43.0, ')', ')', ')', ')', '+', 'cos', '(', 'sin',
                                  '(', 'sin', '(', 34.0, '-', 2.0, '^', 2.0, ')', ')', ')', ')', '+', 'cos',
                                  '(', 1.0, ')', '+', 'cos', '(', 0.0, ')', '^', 3.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [3.0, 'sin', '-', 3.0, 5.0, '*', '-', 'sin', '-', 43.0, 'log10',
                                 'cos', 'sin', '-', 'cos', '-', 34.0, 2.0, 2.0, '^', '-', 'sin', 'sin',
                                 'cos', '+', 'cos', '-', 1.0, 'cos', '+', 0.0, 'cos', 3.0, '^', '+', 'sin'])

    def test37(self):
        list_ = []
        for el in sort_to_polish([2.0, '^', '(', 2.0, '^', 2.0, '*', 2.0, '^', 2.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [2.0, 2.0, 2.0, '^', 2.0, 2.0, '^', '*', '^'])

    def test38(self):
        list_ = []
        for el in sort_to_polish(['sin', '(', 'e', '^', 'log', '(', 'e', '^', 'e', '^', 'sin',
                                  '(', 23.0, ')', ',', 45.0, ')', '+', 'cos', '(', 3.0, '+', 'log10',
                                  '(', 'e', '^', '-', 'e', ')', ')', ')']):
            list_.append(el)
        self.assertEqual(list_, ['e', '^', 'e', 'e', '^', '^', 23.0, ',', 45.0, 'sin', 'log', 3.0, 'e', '^',
                                 'e', '-', 'log10', '+', 'cos', '+', 'sin'])

    # Self-made cases
    def test52(self):
        list_ = []
        for el in sort_to_polish([100.0, '/', 3.0]):
            list_.append(el)
        self.assertEqual(list_, [100.0, 3.0, '/'])

    def test54(self):
        list_ = []
        for el in sort_to_polish([100.0, '+', 3.0]):
            list_.append(el)
        self.assertEqual(list_, [100.0, 3.0, '+'])

    def test55(self):
        list_ = []
        for el in sort_to_polish([100.0, '//', 3.0]):
            list_.append(el)
        self.assertEqual(list_, [100.0, 3.0, '//'])

    def test56(self):
        list_ = []
        for el in sort_to_polish(['sin', '(', 'sin', '(', 1.0, ')', ')']):
            list_.append(el)
        self.assertEqual(list_, [1.0, 'sin', 'sin'])

    def test57(self):
        list_ = []
        for el in sort_to_polish(['sin', '(', 'sin', '(', 1.0, ')', ')', '+', 1.0, '+', 'sin', '(', 1.0, ')']):
            list_.append(el)
        self.assertEqual(list_, [1.0, 'sin', 'sin', 1.0, '+', 1.0, 'sin', '+'])


if __name__ == '__main__':
    unittest.main()
