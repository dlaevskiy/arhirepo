# -*- coding: Windows-1251 -*-
import unittest
import math

from task_alina_epam.math_parser_v1 import calc


class TestCalcing(unittest.TestCase):

    # Unary operators
    def test1(self):
        self.assertEqual(-13, calc([0.0, 13.0, '-']))

    def test2(self):
        self.assertEqual(6 - (-13), calc([6.0, 0.0, 13.0, '-', '-']))

    def test3(self):
        self.assertEqual(1---1, calc([1.0, 1.0, '-']))

    def test4(self):
        self.assertEqual(-+---+-1, calc([0.0, 1.0, '-']))

    def test5(self):
        self.assertEqual(1 + 2 * 2, calc([1.0, 2.0, 2.0, '*', '+']))

    def test6(self):
        self.assertEqual(1 + (2 + 3 * 2) * 3, calc([1.0, 2.0, 3.0, 2.0, '*', '+', 3.0, '*', '+']))

    def test7(self):
        self.assertEqual(10 * (2 + 1), calc([10.0, 2.0, 1.0, '+', '*']))

    def test8(self):
        self.assertEqual(10 ** (2 + 1), calc([10.0, 2.0, 1.0, '+', '^']))

    # TODO: AssertionError: 11 != 11.11111111111111
    def test9(self):
        self.assertEqual(100 / 3 ** 2, calc([100.0, 3.0, 2.0, '^', '/']))

    # TODO: AssertionError: 1 != 1.3333333333333357
    def test10(self):
        self.assertEqual(100 / 3 % 2 ** 2, calc([100.0, 3.0, '/', 2.0, 2.0, '^', '%']))

    # Functions and constants
    def test11(self):
        self.assertEqual(math.pi + math.e, calc(['pi', 'e', '+']))

    def test12(self):
        self.assertEqual(math.log(math.e), calc(['e', 'log']))

    def test13(self):
        self.assertEqual(math.sin(math.pi / 2), calc(['pi', 2.0, '/', 'sin']))

    def test14(self):
        self.assertEqual(math.log10(100), calc([100.0, 'log10']))

    def test15(self):
        self.assertEqual(math.sin(math.pi / 2) * 111 * 6, calc(['pi', 2.0, '/', 'sin', 111.0, '*', 6.0, '*']))

    def test16(self):
        self.assertEqual(2 * math.sin(math.pi / 2), calc([2.0, 'pi', 2.0, '/', 'sin', '*']))

    def test17(self):
        self.assertEqual(abs(-5), calc([0.0, 5.0, '-', 'abs']))

    def test18(self):
        self.assertEqual(round(123.456789), calc([123.456789, 'round']))

    # Associative
    def test19(self):
        self.assertEqual(102 % 12 % 7, calc([102.0,  12.0, '%', 7.0, '%']))

    # TODO: AssertionError: 8 != 8.333333333333334
    def test20(self):
        self.assertEqual(100 / 4 / 3, calc([100.0,  4.0, '/', 3.0, '/']))

    def test21(self):
        self.assertEqual(2 ** 3 ** 4, calc([2.0, 3.0, 4.0, '^', '^']))

    # Comparison operators
    def test22(self):
        self.assertEqual(1 + 2 * 3 == 1 + 2 * 3, calc([1.0, 2.0, 3.0, '*', '+', 1.0, 2.0, 3.0, '*', '+', '==']))

    def test23(self):
        self.assertEqual(math.e ** 5 >= math.e ** 5 + 1, calc(['e', 5.0, '^', 'e', 5.0, '^', 1.0, '+', '>=']))

    def test24(self):
        self.assertEqual(1 + 2 * 4 / 3 + 1 != 1 + 2 * 4 / 3 + 2, calc([1.0, 2.0, 4.0, '*', 3.0, '/', '+', 1.0, '+', 1.0,
                                                                       2.0, 4.0, '*', 3.0, '/', '+', 2.0, '+', '!=']))

    # Common tests
    def test25(self):
        self.assertEqual((100), calc([100.0]))

    def test26(self):
        self.assertEqual(666, calc([666.0]))

    def test27(self):
        self.assertEqual(-.1, calc([0.0, 0.1, '-']))

    # TODO: AssertionError: 0 != 0.3333333333333333
    def test28(self):
        self.assertEqual(1 / 3, calc([1.0, 3.0, '/']))

    def test29(self):
        self.assertEqual(1.0 / 3.0, calc([1.0, 3.0, '/']))

    def test30(self):
        self.assertEqual(.1*2.0**56.0, calc([0.1, 2.0, 56.0, '^',  '*']))

    def test31(self):
        self.assertEqual(math.e ** 34, calc(['e', 34.0, '^']))

    def test32(self):
        self.assertEqual((2.0 ** (math.pi/math.pi+math.e/math.e+2.0**0.0)), calc([2.0, 'pi', 'pi', '/', 'e', 'e', '/',
                                                                                  '+', 2.0, 0.0, '^', '+', '^']))

    def test33(self):
        self.assertEqual((2.0**(math.pi/math.pi+math.e/math.e+2.0**0.0))**(1.0/3.0), calc(
                        [2.0, 'pi', 'pi', '/', 'e', 'e', '/', '+', 2.0, 0.0, '^', '+', '^', 1.0, 3.0, '/', '^']))

    # TODO: TypeError: cannot concatenate 'str' and 'float' objects
    def test34(self):
        self.assertEqual(math.sin(math.pi/2**1) + math.log(1*4+2**2+1, 3**2), calc(['pi', 2.0, 1.0, '^', '/', 'sin',
                                                                                    1.0, 4.0, '*', 2.0, 2.0, '^', '+',
                                                                                    1.0, '+', ',', 3.0, 2.0, '^',
                                                                                    'log', '+']))

    # TODO: AssertionError: 17.06381365110605 != 16.36381365110605
    def test35(self):
        self.assertEqual(10*math.e**0*math.log10(.4 -5/ -0.1-10) - -abs(-53/10) + -5,
                         calc([10.0, 'e', 0.0, '^', '*', 0.4, 5.0, 0.0, 0.1, '-', '/', '-', 10.0, '-', 'log10', '*',
                               0.0, 53.0, 10.0, '/', '-', 'abs', '+', 5.0, '-']))

    def test36(self):
        self.assertEqual(math.sin(-math.cos(-math.sin(3.0)-math.cos(-math.sin(-3.0*5.0)-math.sin(math.cos
                        (math.log10(43.0))))+math.cos(math.sin(math.sin(34.0-2.0**2.0))))--math.cos(1.0)--
                        math.cos(0.0)**3.0), calc([0.0, 0.0, 3.0, 'sin', '-', 0.0, 0.0, 3.0, 5.0, '*', '-', 'sin', '-',
                                                   43.0, 'log10', 'cos', 'sin', '-', 'cos', '-', 34.0, 2.0, 2.0, '^',
                                                   '-', 'sin', 'sin', 'cos', '+', 'cos', '-', 1.0, 'cos', '+', 0.0, 3.0,
                                                   '^', 'cos', '+', 'sin']))

    def test37(self):
        self.assertEqual(2.0**(2.0**2.0*2.0**2.0), calc([2.0, 2.0, 2.0, '^', 2.0, 2.0, '^', '*', '^']))

    # TODO: TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
    def test38(self):
        self.assertEqual(math.sin(math.e**math.log(math.e**math.e**math.sin(23.0), 45.0) +
                                  math.cos(3.0+math.log10(math.e**-math.e))),
                         calc(['e', 'e', 'e', 23.0, 'sin', '^', '^', ',', 45.0, 'log', '^', 3.0, 'e', 0.0, 'e', '-',
                               '^', 'log10', '+', 'cos', '+', 'sin']))

    # Self-made cases
    # TODO: AssertionError: 33 != 33.333333333333336
    def test52(self):
        self.assertEqual(100/3, calc([100.0, 3.0, '/']))

    def test54(self):
        self.assertEqual(100+3, calc([100.0, 3.0, '+']))

    def test55(self):
        self.assertEqual(100//3, calc([100.0, 3.0, '//']))

    def test56(self):
        self.assertEqual(math.sin(math.sin(1)), calc([1.0, 'sin', 'sin']))

    def test57(self):
        self.assertEqual(math.sin(math.sin(1))+1+math.sin(1), calc([1.0, 'sin', 'sin', 1.0, '+', 1.0, 'sin', '+']))

    def test58(self):
        self.assertEqual(abs(-3), calc([0.0, 3.0, '-', 'abs']))

    def test59(self):
        self.assertEqual(round(3.56393), calc([3.56393, 'round']))

    def test60(self):
        self.assertEqual(abs(-round(3.56393)), calc([0.0, 3.56393, 'round', '-', 'abs']))

    # logarithms
    # TODO: AssertionError: 3.0 != 8.0
    def test61(self):
        self.assertEqual(math.log(8, 2), calc([8.0, ',', 2.0, 'log']))

    def test62(self):
        self.assertEqual(math.log(2.7), calc([2.7, 'log']))

    # TODO: AssertionError: 0.0 != 8.0
    def test63(self):
        self.assertEqual((math.log(8, 2)-1)-2, calc([8.0, ',', 2.0, 'log', 1.0, '-', 2.0, '-']))

    # TODO: TypeError: unsupported operand type(s) for -: 'str' and 'float'
    def test64(self):
        self.assertEqual(-math.log(8, 2), calc([0.0, 8.0, ',', 2.0, 'log', '-']))

    # TODO: AssertionError: 2.0 != 8.0
    def test65(self):
        self.assertEqual(math.log(8, 2)-1, calc([8.0, ',', 2.0, 'log', 1.0, '-']))

    # TODO: TypeError: can't multiply sequence by non-int of type 'float'
    def test66(self):
        self.assertEqual(math.log(8, 2)*math.log(16, 2), calc([8.0, ',', 2.0, 'log', 16.0, ',', 2.0, 'log', '*']))

    # TODO: TypeError: can't multiply sequence by non-int of type 'float'
    def test67(self):
        self.assertEqual(math.sin(math.log(8, 2)*math.log(16, 2)), calc([8.0, ',', 2.0, 'log', 16.0, ',', 2.0, 'log',
                                                                         '*', 'sin']))

    # TODO: AssertionError: 3.0 != 27.0
    def test68(self):
        self.assertEqual(math.log(8+20-1, 2+1), calc([8.0, 20.0, '+', 1.0, '-', ',', 2.0,  1.0, '+', 'log']))

    def test69(self):
        self.assertEqual(math.log10(100), calc([100.0, 'log10']))

    # TODO: AssertionError: 2.0 != 100.0
    def test70(self):
        self.assertEqual(math.log(100, 10), calc([100.0, ',', 10.0, 'log']))

    def test71(self):
        self.assertEqual((math.log10(100)-1)-2, calc([100.0, 'log10', 1.0, '-', 2.0, '-']))

    def test72(self):
        self.assertEqual(-math.log10(100), calc([0.0, 100.0, 'log10', '-']))

    def test73(self):
        self.assertEqual(math.log10(100)-1, calc([100.0, 'log10', 1.0, '-']))

    def test74(self):
        self.assertEqual(math.log10(100)*math.log10(1000), calc([100.0, 'log10', 1000.0, 'log10', '*']))

    def test75(self):
        self.assertEqual(math.sin(math.log10(100)*math.log10(1000)), calc([100.0, 'log10', 1000.0, 'log10', '*', 'sin']))

    def test76(self):
        self.assertEqual(math.log10(800/2/4), calc([800.0, 2.0, '/', 4.0, '/', 'log10']))

    # pow
    # TODO: TypeError: pow expected 2 arguments, got 1
    def test77(self):
        self.assertEqual(math.pow(2, 4), calc([2.0, ',', 4.0, 'pow']))

    # TODO: TypeError: pow expected 2 arguments, got 1
    def test78(self):
        self.assertEqual(math.log(math.pow(10, 2), 10), calc([10.0, ',', 2.0, 'pow', ',', 10.0, 'log']))

    # TODO: TypeError: pow expected 2 arguments, got 1
    def test79(self):
        self.assertEqual((math.pow(2, 4)-1)-2, calc([2.0, ',', 4.0, 'pow', 1.0, '-', 2.0, '-']))

    # TODO: TypeError: pow expected 2 arguments, got 1
    def test80(self):
        self.assertEqual(-math.pow(2, 4), calc([0.0, 2.0, ',', 4.0, 'pow', '-']))

    # TODO: TypeError: pow expected 2 arguments, got 1
    def test81(self):
        self.assertEqual(math.pow(2, 4)-1, calc([2.0, ',', 4.0, 'pow', 1.0, '-']))

    # TODO: TypeError: pow expected 2 arguments, got 1
    def test82(self):
        self.assertEqual(math.pow(2, 4)*math.pow(2, 3), calc([2.0, ',', 4.0, 'pow', 2.0, ',', 3.0, 'pow', '*']))

    # TODO: TypeError: pow expected 2 arguments, got 1
    def test83(self):
        self.assertEqual(math.sin(math.pow(2, 4)*math.pow(2, 3)), calc([2.0, ',', 4.0, 'pow', 2.0, ',', 3.0, 'pow', '*',
                                                                        'sin']))

    # TODO: TypeError: pow expected 2 arguments, got 1
    def test84(self):
        self.assertEqual(math.pow(2.0**(2.0**2.0*2.0**2.0), math.log10(100)*math.log10(1000)), calc([2.0, 2.0, 2.0, '^',
                                                                                                     2.0, 2.0, '^', '*',
                                                                                                     '^', ',', 100.0,
                                                                                                     'log10', 1000.0,
                                                                                                     'log10', '*',
                                                                                                     'sin', 'pow']))

    def test85(self):
        self.assertEqual(13, calc([13.0]))

    def test86(self):
        self.assertEqual(-(-13), calc([0.0, 0.0, 13.0, '-', '-']))

    def test87(self):
        self.assertEqual(-(13), calc([0.0, 13.0, '-']))

    def test88(self):
        self.assertEqual(1*-13, calc([1.0, 0.0, 13.0, '-', '*']))

    def test89(self):
        self.assertEqual(1*(-13), calc([1.0, 0.0, 13.0, '-', '*']))

    def test90(self):
        self.assertEqual(1*(13), calc([1.0, 13.0, '*']))

    def test91(self):
        self.assertEqual((1+13), calc([1.0, 13.0, '+']))

    def test92(self):
        self.assertEqual(-1-(-1), calc([0.0, 1.0, '-', 0.0, 1.0, '-', '-']))

    def test93(self):
        self.assertEqual(((1)), calc([1.0]))

    def test94(self):
        self.assertEqual(-(-(-1)), calc([0.0, 0.0, 0.0, 1.0, '-', '-', '-']))

if __name__ == '__main__':
    unittest.main()
