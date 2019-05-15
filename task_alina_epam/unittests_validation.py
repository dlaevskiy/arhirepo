import unittest
# task_alina_epam.
from math_parser_v1 import validate_parsed_list


class ExpectedFailureTestCase(unittest.TestCase):
    # Error cases
    def test1(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list([]))

    def test2(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['+']))

    def test3(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list([1.0, '-']))

    def test4(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['ee']))

    def test5(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['==', 7.0]))

    def test6(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list([1.0, '+', 2.0, '(', 3.0, '*', 4.0, ')', ')']))

    def test7(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', '(', 1.0, '+', 2.0, ')']))

    def test8(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', ')']))

    def test9(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['log10', 0.0, '(', 100.0, ')']))

    def test10(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['-', '-', '-', '-', '-', '-']))

    def test11(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', ')']))

    def test12(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list([6.0, '*', '*', 6.0]))

    def test13(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', ')']))

    def test14(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', '(', '(', '(', '(', ]))

    def test15(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['pow', '(', 2.0, ',', 3.0, ',', 4.0, ')']))

    def test16(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list([77.0, '==', '==', 77.0]))

    def test17(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list([1.0, '+', '&', 6.0]))

    def test18(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['_', '+', 'son']))

    def test19(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', '.', 77.0, '-', 4.0, ')', '+', 2.0]))

    def test20(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', ',', 77.0, '-', 4.0, ')', '+', 2.0]))

    def test21(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', '//', 77.0, '-', 4.0, ')', '+', 2.0]))

    def test22(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', 1.0, '+', 5.0, ')', '(', 1.0, '+', 5.0, ')']))

    def test19(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', '.', 77.0, '-', 4.0, ')', '+', 2.0]))

    def test20(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', ',', 77.0, '-', 4.0, ')', '+', 2.0]))

    def test21(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', '//', 77.0, '-', 4.0, ')', '+', 2.0]))


class ExpectedSuccessTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['-', 13.0]))

    def test_2(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([6.0, '-', '(', '-', 13.0, ')']))

    def test_3(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([1.0, '-', '-', '-', 1.0]))

    def test_4(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['-', '+', '-', '-', '-', '+', '-', 1.0]))

    def test_5(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([1.0, '+', 2.0, '*', 2.0]))

    def test_6(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([1.0, '+', '(', 2.0, '+', 3.0, '*', 2.0, ')', '*', 3.0]))

    def test_7(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([10.0, '*', '(', 2.0, '+', 1.0, ')']))

    def test_8(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([10.0, '^', '(', 2.0, '+', 1.0, ')']))

    def test_9(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([100.0, '/', 3.0, '^', 2.0]))

    def test_10(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([100.0, '/', 3.0, '%', 2.0, '^', 2.0]))

    def test_11(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['pi', '+', 'e']))

    def test_12(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['log', '(', 'e', ')']))

    def test_13(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['sin', '(', 'pi', '/', 2.0, ')']))

    def test_14(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['log10', '(', 100.0, ')']))

    def test_15(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                    ['sin', '(', 'pi', '/', 2.0, ')', '*', 111.0, '*', 6.0]))

    def test_16(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                    [2.0, '*', 'sin', '(', 'pi', '/', 2.0, ')']))

    def test_17(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['abs', '(', '-', 5.0, ')']))

    def test_18(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['round', '(', 123.456789, ')']))

    def test_19(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([102.0, '%', 12.0, '%', 7.0]))

    def test_20(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([100.0, '/', 4.0, '/', 3.0]))

    def test_21(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([2.0, '^', 3.0, '^', 4.0]))

    def test_22(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                    [1.0, '+', 2.0, '*', 3.0, '==', 1.0, '+', 2.0, '*', 3.0]))

    def test_23(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                    ['e', '^', 5.0, '>=', 'e', '^', 5.0, '+', 1.0]))

    def test_24(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                    [1.0, '+', 2.0, '*', 4.0, '/', 3.0, '+', 1.0, '!=', 1.0, '+', 2.0, '*', 4.0, '/', 3.0, '+', 2.0]))

    def test_25(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['(', 100.0, ')']))

    def test_26(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([666.0]))

    def test_27(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(['-', 0.1]))

    def test_28(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([1.0, '/', 3.0]))

    def test_29(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list([0.1, '*', 2.0, '^', 56.0]))

    def test_30(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list('e', '^', 34.0))

    def test_31(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                ['(', 2.0, '^', '(', 'pi', '/', 'pi', '+', 'e', '/', 'e', '+', 2.0, '^', 0.0, ')', ')']))

    def test_32(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                ['(', 2.0, '^', '(', 'pi', '/', 'pi', '+', 'e', '/', 'e', '+', 2.0, '^', 0.0, ')', ')',
                                 '^', '(', 1.0, '/', 3.0, ')']))

    def test_33(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                [10.0, '*', 'e', '^', 0.0, '*', 'log10', '(', 0.4, '-', 5.0, '/', '-', 0.1, '-',
                                 10.0, ')', '-', '-', 'abs', '(', '-', 53.0, '/', 10.0, ')', '+', '-', 5.0]))

    def test_34(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                ['sin', '(', '-', 'cos', '(', '-', 'sin', '(', 3.0, ')', '-', 'cos',
                                 '(', '-', 'sin', '(', '-', 3.0, '*', 5.0, ')', '-', 'sin', '(', 'cos', '(',
                                 'log10', '(', 43.0, ')', ')', ')', ')', '+', 'cos', '(', 'sin', '(', 'sin', '(',
                                 34.0, '-', 2.0, '^', 2.0, ')', ')', ')', ')', '-', '-', 'cos', '(', 1.0, ')', '-', '-',
                                 'cos', '(', 0.0, ')', '^', 3.0, ')']))

    def test_35(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                [2.0, '^', '(', 2.0, '^', 2.0, '*', 2.0, '^', 2.0, ')']))

    def test_36(self):
        self.assertEqual('Formula was validated! Errors were not found.', lambda: validate_parsed_list(
                                ['sin', '(', 'e', '^', 'log', '(', 'e', '^', 'e', '^', 'sin', '(', 23.0, ')', ',', 45.0,
                                 ')', '+', 'cos', '(', 3.0, '+', 'log10', '(', 'e', '^', '-', 'e', ')', ')', ')']))
