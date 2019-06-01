import unittest

from task_alina_epam.math_parser_v1 import pre_validation


class TestParsingNegativeCases(unittest.TestCase):
    def test1(self):
        self.assertRaises(ValueError, lambda: pre_validation('1+&6.0'))

    def test86(self):
        self.assertRaises(ValueError, lambda: pre_validation('1+6.0&'))

    def test87(self):
        self.assertRaises(ValueError, lambda: pre_validation('_5+6'))

    def test88(self):
        self.assertRaises(ValueError, lambda: pre_validation('5_+6'))

    def test89(self):
        self.assertRaises(ValueError, lambda: pre_validation('1>=@'))

    def test90(self):
        self.assertRaises(ValueError, lambda: pre_validation('1@>=9'))

    def test91(self):
        self.assertRaises(ValueError, lambda: pre_validation('-2+(#+1)'))

    def test92(self):
        self.assertRaises(ValueError, lambda: pre_validation('abs(@)'))

    def test93(self):
        self.assertRaises(ValueError, lambda: pre_validation('round(@)'))

    def test94(self):
        self.assertRaises(ValueError, lambda: pre_validation('sin(5+@)'))

    def test95(self):
        self.assertRaises(ValueError, lambda: pre_validation('sin(@+5)'))

    def test96(self):
        self.assertRaises(ValueError, lambda: pre_validation('(5+@)/7'))

    def test97(self):
        self.assertRaises(ValueError, lambda: pre_validation('1+#+6'))

    def test98(self):
        self.assertRaises(ValueError, lambda: pre_validation('1+#8+6'))

    # Number with more than one delimiter
    def test99(self):
        self.assertRaises(ValueError, lambda: pre_validation('1..5'))

    def test100(self):
        self.assertRaises(ValueError, lambda: pre_validation('-1..5'))

    def test101(self):
        self.assertRaises(ValueError, lambda: pre_validation('1..5+3..7'))

    def test102(self):
        self.assertRaises(ValueError, lambda: pre_validation('1..5+3'))

    def test103(self):
        self.assertRaises(ValueError, lambda: pre_validation('3+1..5'))

    def test104(self):
        self.assertRaises(ValueError, lambda: pre_validation('1+1..5-4'))

    def test105(self):
        self.assertRaises(ValueError, lambda: pre_validation('sin(1..5)'))

    def test106(self):
        self.assertRaises(ValueError, lambda: pre_validation('(1..5+3)/2'))

    def test107(self):
        self.assertRaises(ValueError, lambda: pre_validation('round(1..5)'))

    def test108(self):
        self.assertRaises(ValueError, lambda: pre_validation('abs(-1..5)'))

    def test109(self):
        self.assertRaises(ValueError, lambda: pre_validation('1>=1..5'))

    def test110(self):
        self.assertRaises(ValueError, lambda: pre_validation(''))

    def test111(self):
        self.assertRaises(ValueError, lambda: pre_validation(None))

    def test112(self):
        self.assertRaises(ValueError, lambda: pre_validation(18))


if __name__ == '__main__':
    unittest.main()
