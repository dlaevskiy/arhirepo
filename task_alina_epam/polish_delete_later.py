import unittest

from task_alina_epam.math_parser_v1 import sort_to_polish


class TestSorting(unittest.TestCase):
    # # TODO: process log correctly (if we put arguments of logs in (), everything will be done correctly)
    # def test68(self):  # log(8+20-1, 2+1)
    #     list_ = []
    #     for el in sort_to_polish(['log', '(', 8.0, '+', 20.0, '-', 1.0, ',', 2.0, '+', 1.0, ')']):
    #         list_.append(el)
    #     self.assertEqual(list_, [8.0, 20.0, '+', 1.0, '-', ',', 2.0, 1.0, '+', 'log'])

    # # TODO: problem, when unary operations go after binary without parentheses
    # def test88(self):
    #     list_ = []
    #     for el in sort_to_polish([1.0, '*', '-', 13.0]):
    #         list_.append(el)
    #     self.assertEqual(list_, [1.0, 0.0, 13.0, '-', '*'])

    # TODO: process log correctly (if we put here first argument of log in (), everything will be done correctly)
    # TODO: problem, when unary operations go after binary without parentheses as e^-e
    def test38(self):  # sin(e^log(e^e^sin(23.0),45.0) + cos(3.0+log10(e^-e)))
        list_ = []
        for el in sort_to_polish(['sin', '(', 'e', '^', 'log', '(', 'e', '^', 'e', '^', 'sin',
                                  '(', 23.0, ')', ',', 45.0, ')', '+', 'cos', '(', 3.0, '+', 'log10',
                                  '(', 'e', '^', '-', 'e', ')', ')', ')']):
            list_.append(el)
        self.assertEqual(list_, ['e', 'e', 'e', 23.0, 'sin', '^', '^',  ',',
                                 45.0, 'log', '^',
                                 3.0, 'e', 0.0, 'e', '-', '^', 'log10', '+', 'cos', '+',
                                 'sin'])
