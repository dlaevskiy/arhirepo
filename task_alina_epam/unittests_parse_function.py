import unittest

from task_alina_epam.math_parser_v1 import parse


class TestParsing(unittest.TestCase):

    # Unary operators
    def test1(self):
        list_ = []
        for el in parse('-13'):
            list_.append(el)
        self.assertEqual(list_, ['-', 13.0])

    def test2(self):
        list_ = []
        for el in parse('6-(-13)'):
            list_.append(el)
        self.assertEqual(list_, [6.0, '-', '(', '-', 13.0, ')'])

    def test3(self):
        list_ = []
        for el in parse('1---1'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '-', '-', '-', 1.0])

    def test4(self):
        list_ = []
        for el in parse('-+---+-1'):
            list_.append(el)
        self.assertEqual(list_, ['-', '+', '-', '-', '-', '+', '-', 1.0])

    # Operation priority
    def test5(self):
        list_ = []
        for el in parse('1+2*2'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', 2.0, '*', 2.0])

    def test6(self):
        list_ = []
        for el in parse('1+(2+3*2)*3'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', '(', 2.0, '+', 3.0, '*', 2.0, ')', '*', 3.0])

    def test7(self):
        list_ = []
        for el in parse('10*(2+1)'):
            list_.append(el)
        self.assertEqual(list_, [10.0, '*', '(', 2.0, '+', 1.0, ')'])

    def test8(self):
        list_ = []
        for el in parse('10^(2+1)'):
            list_.append(el)
        self.assertEqual(list_, [10.0, '^', '(', 2.0, '+', 1.0, ')'])

    def test9(self):
        list_ = []
        for el in parse('100/3^2'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 3.0, '^', 2.0])

    def test10(self):
        list_ = []
        for el in parse('100/3%2^2'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 3.0, '%', 2.0, '^', 2.0])

    # Functions and constants
    def test11(self):
        list_ = []
        for el in parse('pi+e'):
            list_.append(el)
        self.assertEqual(list_, ['pi', '+', 'e'])

    def test12(self):
        list_ = []
        for el in parse('log(e)'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 'e', ')'])

    def test13(self):
        list_ = []
        for el in parse('sin(pi/2)'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'pi', '/', 2.0, ')'])

    def test14(self):
        list_ = []
        for el in parse('log10(100)'):
            list_.append(el)
        self.assertEqual(list_, ['log10', '(', 100.0, ')'])

    def test15(self):
        list_ = []
        for el in parse('sin(pi/2)*111*6'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'pi', '/', 2.0, ')', '*', 111.0, '*', 6.0])

    def test16(self):
        list_ = []
        for el in parse('2*sin(pi/2)'):
            list_.append(el)
        self.assertEqual(list_, [2.0, '*', 'sin', '(', 'pi', '/', 2.0, ')'])

    def test17(self):
        list_ = []
        for el in parse('abs(-5)'):
            list_.append(el)
        self.assertEqual(list_, ['abs', '(', '-', 5.0, ')'])

    def test18(self):
        list_ = []
        for el in parse('round(123.456789)'):
            list_.append(el)
        self.assertEqual(list_, ['round', '(', 123.456789, ')'])

    # Associative
    def test19(self):
        list_ = []
        for el in parse('102%12%7'):
            list_.append(el)
        self.assertEqual(list_, [102.0, '%', 12.0, '%', 7.0])

    def test20(self):
        list_ = []
        for el in parse('100/4/3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 4.0, '/', 3.0])

    def test21(self):
        list_ = []
        for el in parse('2^3^4'):
            list_.append(el)
        self.assertEqual(list_, [2.0, '^', 3.0, '^', 4.0])

    # Comparison operators
    def test22(self):
        list_ = []
        for el in parse('1+2*3==1+2*3'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', 2.0, '*', 3.0, '==', 1.0, '+', 2.0, '*', 3.0])

    def test23(self):
        list_ = []
        for el in parse('e^5>=e^5+1'):
            list_.append(el)
        self.assertEqual(list_, ['e', '^', 5.0, '>=', 'e', '^', 5.0, '+', 1.0])

    def test24(self):
        list_ = []
        for el in parse('1+2*4/3+1!=1+2*4/3+2'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', 2.0, '*', 4.0, '/', 3.0, '+', 1.0, '!=', 1.0, '+',
                                 2.0, '*', 4.0, '/', 3.0, '+', 2.0])

    # Common tests
    def test25(self):
        list_ = []
        for el in parse('(100)'):
            list_.append(el)
        self.assertEqual(list_, ['(', 100.0, ')'])

    def test26(self):
        list_ = []
        for el in parse('666'):
            list_.append(el)
        self.assertEqual(list_, [666.0])

    def test27(self):
        list_ = []
        for el in parse('-.1'):
            list_.append(el)
        self.assertEqual(list_, ['-', 0.1])

    def test28(self):
        list_ = []
        for el in parse('1/3'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '/', 3.0])

    def test29(self):
        list_ = []
        for el in parse('1.0/3.0'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '/', 3.0])

    def test30(self):
        list_ = []
        for el in parse('.1 * 2.0^56.0'):
            list_.append(el)
        self.assertEqual(list_, [0.1, '*', 2.0, '^', 56.0])

    def test31(self):
        list_ = []
        for el in parse('e^34'):
            list_.append(el)
        self.assertEqual(list_, ['e', '^', 34.0])

    def test32(self):
        list_ = []
        for el in parse('(2.0^(pi/pi+e/e+2.0^0.0))'):
            list_.append(el)
        self.assertEqual(list_, ['(', 2.0, '^', '(', 'pi', '/', 'pi', '+', 'e', '/', 'e', '+', 2.0, '^', 0.0, ')', ')'])

    def test33(self):
        list_ = []
        for el in parse('(2.0^(pi/pi+e/e+2.0^0.0))^(1.0/3.0)'):
            list_.append(el)
        self.assertEqual(list_, ['(', 2.0, '^', '(', 'pi', '/', 'pi', '+', 'e', '/', 'e', '+', 2.0, '^', 0.0,
                                 ')', ')', '^', '(', 1.0, '/', 3.0, ')'])

    # def test34(self):  # how to process comma in log
    #     list_ = []
    #     for el in parse('sin(pi/2^1) + log(1*4+2^2+1, 3^2)'):
    #         list_.append(el)
    #     self.assertEqual(list_, ['sin', '(', 'pi', '/', 2.0, '^', 1.0, ')', '+', 'log', '(', 1.0, '*', 4.0, '+',
    #                              2.0, '^', 2.0, '+', 1.0, ',', 3.0, '^', 2.0, ')'])

    def test35(self):  # why there are no parentheses after division in log
        list_ = []
        for el in parse('10*e^0*log10(.4 -5/ -0.1-10) - -abs(-53/10) + -5'):
            list_.append(el)
        self.assertEqual(list_, [10.0, '*', 'e', '^', 0.0, '*', 'log10', '(', 0.4, '-', 5.0, '/', '-', 0.1, '-',
                                 10.0, ')', '-', '-', 'abs', '(', '-', 53.0, '/', 10.0, ')', '+', '-', 5.0])

    def test36(self):
        list_ = []
        for el in parse('sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))+'
                        'cos(sin(sin(34.0-2.0^2.0))))--cos(1.0)--cos(0.0)^3.0)'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', '-', 'cos', '(', '-', 'sin', '(', 3.0, ')', '-', 'cos',
                                 '(', '-', 'sin', '(', '-', 3.0, '*', 5.0, ')', '-', 'sin', '(', 'cos', '(',
                                 'log10', '(', 43.0, ')', ')', ')', ')', '+', 'cos', '(', 'sin', '(', 'sin', '(',
                                 34.0, '-', 2.0, '^', 2.0, ')', ')', ')', ')', '-', '-', 'cos', '(', 1.0, ')', '-', '-',
                                 'cos', '(', 0.0, ')', '^', 3.0, ')'])

    def test37(self):
        list_ = []
        for el in parse('2.0^(2.0^2.0*2.0^2.0)'):
            list_.append(el)
        self.assertEqual(list_, [2.0, '^', '(', 2.0, '^', 2.0, '*', 2.0, '^', 2.0, ')'])

    def test38(self):
        list_ = []
        for el in parse('sin(e^log(e^e^sin(23.0),45.0) + cos(3.0+log10(e^-e)))'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'e', '^', 'log', '(', 'e', '^', 'e', '^', 'sin', '(', 23.0, ')', ',',
                                 45.0, ')', '+', 'cos', '(', 3.0, '+', 'log10', '(', 'e', '^', '-', 'e', ')', ')', ')'])

    # Error cases
    def test39(self):
        list_ = []
        for el in parse(''):
            list_.append(el)
        self.assertEqual(list_, [])

    def test40(self):
        list_ = []
        for el in parse('+'):
            list_.append(el)
        self.assertEqual(list_, ['+'])

    def test41(self):
        list_ = []
        for el in parse('1-'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '-'])

    def test42(self):
        list_ = []
        for el in parse('ee'):
            list_.append(el)
        self.assertEqual(list_, ['ee'])

    def test43(self):
        list_ = []
        for el in parse('==7'):
            list_.append(el)
        self.assertEqual(list_, ['==', 7.0])

    def test44(self):
        list_ = []
        for el in parse('1 + 2(3 * 4))'):
            list_.append(el)
        self.assertEqual(list_, [1.0, '+', 2.0, '(', 3.0, '*', 4.0, ')', ')'])

    def test45(self):
        list_ = []
        for el in parse('((1+2)'):
            list_.append(el)
        self.assertEqual(list_, ['(', '(', 1.0, '+', 2.0, ')'])

    def test46(self):
        list_ = []
        for el in parse('log100(100)'):
            list_.append(el)
        self.assertEqual(list_, ['log100', '(', 100.0, ')'])

    def test47(self):
        list_ = []
        for el in parse('------'):
            list_.append(el)
        self.assertEqual(list_, ['-', '-', '-', '-', '-', '-'])

    def test48(self):
        list_ = []
        for el in parse('6 * * 6'):
            list_.append(el)
        self.assertEqual(list_, [6.0, '*', '*', 6.0])

    def test49(self):
        list_ = []
        for el in parse('((((('):
            list_.append(el)
        self.assertEqual(list_, ['(', '(', '(', '(', '(', ])

    def test50(self):  # how to process commas in pow
        list_ = []
        for el in parse('pow(2, 3, 4)'):
            list_.append(el)
        self.assertEqual(list_, ['pow', '(', 2.0, ',', 3.0, ',', 4.0, ')'])

    # Self-made cases
    def test51(self):
        list_ = []
        for el in parse('77====77'):
            list_.append(el)
        self.assertEqual(list_, [77.0, '==', '==', 77.0])

    def test52(self):
        list_ = []
        for el in parse('100/3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '/', 3.0])

    def test53(self):
        list_ = []
        for el in parse('100=3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '=', 3.0])

    def test54(self):
        list_ = []
        for el in parse('100+3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '+', 3.0])

    def test55(self):
        list_ = []
        for el in parse('100//3'):
            list_.append(el)
        self.assertEqual(list_, [100.0, '//', 3.0])

    def test56(self):
        list_ = []
        for el in parse('sin(sin(1))'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'sin', '(', 1.0, ')', ')'])

    def test57(self):
        list_ = []
        for el in parse('sin(sin(1))+1+sin(1)'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'sin', '(', 1.0, ')', ')', '+', 1.0, '+', 'sin', '(', 1.0, ')'])

    def test58(self):
        list_ = []
        for el in parse('log100l(100)'):
            list_.append(el)
        self.assertEqual(list_, ['log100l', '(', 100.0, ')'])

    def test59(self):
        list_ = []
        for el in parse('log100+(100)'):
            list_.append(el)
        self.assertEqual(list_, ['log100', '+', '(', 100.0, ')'])

    def test60(self):
        list_ = []
        for el in parse('.+1'):
            list_.append(el)
        self.assertEqual(list_, ['.', '+', 1.0, ])

    #logarithms
    def test61(self):
        list_ = []
        for el in parse('log(8,2)'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 8.0, ',', 2.0, ')'])

    def test62(self):
        list_ = []
        for el in parse('log(2.7)'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 2.7, ')'])

    def test63(self):
        list_ = []
        for el in parse('(log(8,2)-1)-2'):
            list_.append(el)
        self.assertEqual(list_, ['(', 'log', '(', 8.0, ',', 2.0, ')', '-', 1.0, ')', '-', 2.0])

    def test64(self):
        list_ = []
        for el in parse('-log(8,2)'):
            list_.append(el)
        self.assertEqual(list_, ['-', 'log', '(', 8.0, ',', 2.0, ')'])

    def test65(self):
        list_ = []
        for el in parse('log(8,2)-1'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 8.0, ',', 2.0, ')', '-', 1.0])

    def test66(self):
        list_ = []
        for el in parse('log(8,2)*log(16,2)'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 8.0, ',', 2.0, ')', '*', 'log', '(', 16.0, ',', 2.0, ')'])

    def test67(self):
        list_ = []
        for el in parse('sin(log(8,2)*log(16,2))'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'log', '(', 8.0, ',', 2.0, ')', '*', 'log', '(', 16.0, ',', 2.0, ')', ')'])

    def test68(self):
        list_ = []
        for el in parse('log(8+20-1,2+1)'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 8.0, '+', 20.0, '-', 1.0, ',', 2.0, '+', 1.0, ')'])

    def test69(self):
        list_ = []
        for el in parse('log10(100)'):
            list_.append(el)
        self.assertEqual(list_, ['log10', '(', 100.0, ')'])

    def test70(self):
        list_ = []
        for el in parse('log(100,10)'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 100.0, ',', 10.0, ')'])

    def test71(self):
        list_ = []
        for el in parse('(log10(100)-1)-2'):
            list_.append(el)
        self.assertEqual(list_, ['(', 'log10', '(', 100.0, ')', '-', 1.0, ')', '-', 2.0])

    def test72(self):
        list_ = []
        for el in parse('-log10(100)'):
            list_.append(el)
        self.assertEqual(list_, ['-', 'log10', '(', 100.0, ')'])

    def test73(self):
        list_ = []
        for el in parse('log10(100)-1'):
            list_.append(el)
        self.assertEqual(list_, ['log10', '(', 100.0, ')', '-', 1.0])

    def test74(self):
        list_ = []
        for el in parse('log10(100)*log10(1000)'):
            list_.append(el)
        self.assertEqual(list_, ['log10', '(', 100.0, ')', '*', 'log10', '(', 1000.0, ')'])

    def test75(self):
        list_ = []
        for el in parse('sin(log10(100)*log10(1000))'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'log10', '(', 100.0, ')', '*', 'log10', '(', 1000.0, ')', ')'])

    def test76(self):
        list_ = []
        for el in parse('log10(800/2/4)'):
            list_.append(el)
        self.assertEqual(list_, ['log10', '(', 800.0, '/', 2.0, '/', 4.0, ')'])

    # pow
    def test77(self):
        list_ = []
        for el in parse('pow(2,4)'):
            list_.append(el)
        self.assertEqual(list_, ['pow', '(', 2.0, ',', 4.0, ')'])

    def test78(self):
        list_ = []
        for el in parse('log(pow(10,2),10)'):
            list_.append(el)
        self.assertEqual(list_, ['log', '(', 'pow', '(', 10.0, ',', 2.0, ')', ',', 10.0, ')'])

    def test79(self):
        list_ = []
        for el in parse('(pow(2,4)-1)-2'):
            list_.append(el)
        self.assertEqual(list_, ['(', 'pow', '(', 2.0, ',', 4.0, ')', '-', 1.0, ')', '-', 2.0])

    def test80(self):
        list_ = []
        for el in parse('-pow(2,4)'):
            list_.append(el)
        self.assertEqual(list_, ['-', 'pow', '(', 2.0, ',', 4.0, ')'])

    def test81(self):
        list_ = []
        for el in parse('pow(2,4)-1'):
            list_.append(el)
        self.assertEqual(list_, ['pow', '(', 2.0, ',', 4.0, ')', '-', 1.0])

    def test82(self):
        list_ = []
        for el in parse('pow(2,4)*pow(2,3)'):
            list_.append(el)
        self.assertEqual(list_, ['pow', '(', 2.0, ',', 4.0, ')', '*', 'pow', '(', 2.0, ',', 3.0, ')'])

    def test83(self):
        list_ = []
        for el in parse('sin(pow(2,4)*pow(2,3))'):
            list_.append(el)
        self.assertEqual(list_, ['sin', '(', 'pow', '(', 2.0, ',', 4.0, ')', '*', 'pow', '(', 2.0, ',', 3.0, ')', ')'])

    def test84(self):
        list_ = []
        for el in parse('pow(2.0^(2.0^2.0*2.0^2.0),sin(log10(100)*log10(1000)))'):
            list_.append(el)
        self.assertEqual(list_, ['pow', '(', 2.0, '^', '(', 2.0, '^', 2.0, '*', 2.0, '^', 2.0, ')', ',', 'sin', '(',
                                 'log10', '(', 100.0, ')', '*', 'log10', '(', 1000.0, ')', ')', ')'])

    # Incorrect symbol in formula
    def test85(self):
        self.assertRaises(ValueError, lambda: parse('1+&6.0'))

    def test86(self):
        self.assertRaises(ValueError, lambda: parse('1+6.0&'))

    def test87(self):
        self.assertRaises(ValueError, lambda: parse(['_5+6']))

    def test88(self):
        self.assertRaises(ValueError, lambda: parse(['5_+6']))

    def test89(self):
        self.assertRaises(ValueError, lambda: parse(['1>=@']))

    def test90(self):
        self.assertRaises(ValueError, lambda: parse(['1@>=9']))

    def test91(self):
        self.assertRaises(ValueError, lambda: parse(['-2+(#+1)']))

    def test92(self):
        self.assertRaises(ValueError, lambda: parse(['abs(@)']))

    def test93(self):
        self.assertRaises(ValueError, lambda: parse(['round(@)']))

    def test94(self):
        self.assertRaises(ValueError, lambda: parse(['sin(5+@)']))

    def test95(self):
        self.assertRaises(ValueError, lambda: parse(['sin(@+5)']))

    def test96(self):
        self.assertRaises(ValueError, lambda: parse(['(5+@)/7']))

    def test97(self):
        self.assertRaises(ValueError, lambda: parse(['1+#+6']))

    def test98(self):
        self.assertRaises(ValueError, lambda: parse(['1+#8+6']))

    # Number with more than one delimiter
    def test99(self):
        self.assertRaises(ValueError, lambda: parse(['1..5']))

    def test100(self):
        self.assertRaises(ValueError, lambda: parse(['-1..5']))

    def test101(self):
        self.assertRaises(ValueError, lambda: parse(['1..5+3..7']))

    def test102(self):
        self.assertRaises(ValueError, lambda: parse(['1..5+3']))

    def test103(self):
        self.assertRaises(ValueError, lambda: parse(['3+1..5']))

    def test104(self):
        self.assertRaises(ValueError, lambda: parse(['1+1..5-4']))

    def test105(self):
        self.assertRaises(ValueError, lambda: parse(['sin(1..5)']))

    def test106(self):
        self.assertRaises(ValueError, lambda: parse(['(1..5+3)/2']))

    def test107(self):
        self.assertRaises(ValueError, lambda: parse(['round(1..5)']))

    def test108(self):
        self.assertRaises(ValueError, lambda: parse(['abs(-1..5)']))

    def test109(self):
        self.assertRaises(ValueError, lambda: parse(['1>=1..5']))

if __name__ == '__main__':
    unittest.main()
