import unittest

from task_alina_epam.math_parser_v1 import validate_parsed_list


class ExpectedFailureTestCase(unittest.TestCase):

    def test1(self):
        self.assertRaises(ValueError, lambda: validate_parsed_list(['(', ')']))

