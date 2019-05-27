import argparse
from sys import argv


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(argv[1:])
    parsed_formula = validate_parsed_list(parse(formula_string))
    polish_list = sort_to_polish(parsed_formula)
    result = calc(polish_list)
    print result


# parser = argparse.ArgumentParser(prog='pycalc', description='Pure-python command-line calculator.')
# parser.add_argument('string', metavar='EXPRESSION', type=str, nargs='+',
#                     help='expression string to evaluate')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print args.accumulate(args.integers)
