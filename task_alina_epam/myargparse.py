import argparse
from sys import argv

from task_alina_epam.math_parser_v1 import (pre_validation,
                                            parse,
                                            validate_parsed_list,
                                            process_unary_operations,
                                            sort_to_polish,
                                            calc)


def createParser():
    parser = argparse.ArgumentParser(prog='Py Calc',
                                     description='Pure-python command-line calculator',
                                     epilog='(c) Alina Laevskaya 2019.'
                                     )

    parser.add_argument('-f', '--formula', help='Send formula for processing.')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(argv[1:])
    pre_validation(namespace.formula)
    print('Prevalidation was done!')
    parsed_list = []
    for el in parse(namespace.formula):
        parsed_list.append(el)
    print('Formula was parsed to tokens.')
    print(validate_parsed_list(parsed_list))
    print('Validation was done!')
    parsed_list = process_unary_operations(parsed_list)
    print('Redundant unary operations were deleted!')
    polish_list = []
    for el in sort_to_polish(parsed_list):
        polish_list.append(el)
    print('Tokens were sorted to polish list!')
    result = calc(polish_list)
    print('Result of calculating of {} is {}'.format(namespace.formula, result))
