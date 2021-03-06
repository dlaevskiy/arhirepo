# -*- coding: Windows-1251 -*-
import sys
import math
import string
import operator
import inspect

LETTERS = tuple(string.ascii_lowercase + string.ascii_uppercase)
DIGITS = tuple(string.digits)

UNARY_OPERATORS = {'+': (1, operator.add),
                   '-': (1, operator.sub),
                   }

BINARY_OPERATORS = {'*': (2, operator.mul),
                    '/': (2, operator.truediv),
                    '//': (2, operator.floordiv),
                    '%': (2, operator.imod),
                    '^': (3, operator.ipow),
                    '<': (0, operator.lt),
                    '<=': (0, operator.le),
                    '>': (0, operator.gt),
                    '>=': (0, operator.ge),
                    '==': (0, operator.eq),
                    '!=': (0, operator.ne),
                    }

OPERATORS = UNARY_OPERATORS.copy()
OPERATORS.update(BINARY_OPERATORS)

PARENTHESES = ('(', ')')

OPERATORS_BEGIN = ('+', '-', '*', '/', '%', '^', '<', '>', '=', '!',)

DOUBLE_OPER_PART1 = ('/', '<', '>', '=', '!',)
DOUBLE_OPER_PART2 = ('/', '=',)

BUILT_IN_FUNCTIONS = ('abs', 'round')
NOT_SUPPORTED_MATH_FUNCTIONS = ('frexp', 'isclose', 'isinf', 'isfinite', 'isnan')
MATH_CONSTS = ('e', 'pi', 'inf', 'nan', 'tau')
MATH_FUNCTIONS = tuple([func for func in dir(math) if not func.startswith('_') and
                        func not in (MATH_CONSTS + NOT_SUPPORTED_MATH_FUNCTIONS)])

ALL_FUNCTIONS = BUILT_IN_FUNCTIONS + MATH_FUNCTIONS
ALL_FUNCTIONS_AND_CONSTS = ALL_FUNCTIONS + MATH_CONSTS

ALL_FUNCTIONS_DICT = {el: (4,) for el in ALL_FUNCTIONS}
ALL_FUNCTIONS_AND_OPERATORS_DICT = ALL_FUNCTIONS_DICT.copy()
ALL_FUNCTIONS_AND_OPERATORS_DICT.update(OPERATORS)


DELIMETERS = ('.', ',', ' ')
ALLOWED_TOKENS = OPERATORS_BEGIN + LETTERS + DIGITS + PARENTHESES + DELIMETERS


def excepthook(type, value, traceback):
    print(value)


sys.excepthook = excepthook


def matched_parentheses(el, count):
    if el == "(":
        count += 1
    elif el == ")":
        count -= 1
    return count


def pre_validation(formula_string):
    # ��������, ��� ������� �� ������ ������
    if not isinstance(formula_string, str) or not formula_string:
        raise ValueError('Formula should be non empty string!')
    # ���������, ��� � ������� ��� ����� ������ ����������� ������
    # � ������� ���������� ������� ������� ��� �����, ����� ��������� ���������� ������� �� ������
    if '..' in formula_string:
        raise ValueError('Number can not contain more than one delimiter "." !')
    # �������� �� ����������� ��������
    for el in formula_string.strip():
        if el not in ALLOWED_TOKENS:
            raise ValueError('Formula contains incorrect symbol "{}"'.format(el))


def parse(formula_string):
    number = ''  # ��� ���������� �����
    op = ''  # ��� ���������� ����������
    function = ''  # ��� ���������� �������
    for el in formula_string.strip():
        if el in LETTERS:  # ��������� �������
            function += el.lower()
            if op:  # ���������� ��������, ���� ��� ��������
                yield op
                op = ''
            if number:  # ���������� �����, ���� ���� ���������
                yield float(number) if number != '.' else '.'
                number = ''
        elif el in string.digits + '.':  # ��������� ����� ����� � � ������
            if function:
                function += el  # ���������� ����������� �������, ���� �� �������� ���-�� �������� �� �����
            else:
                number += el
                if op:  # ���������� ��������, ���� ��� ��������
                    yield op
                    op = ''
                if function:  # ���������� �������, ���� ���� ���������
                    yield function
                    function = ''
        elif el in OPERATORS_BEGIN:  # ��������� ����������
            if el in DOUBLE_OPER_PART1 and not op:  # ���� �������� ������� ��������, �������� � ���
                op += el
            elif el in DOUBLE_OPER_PART2 and op:  # ������ �������
                op += el
                if number:  # ���������� �����, ���� ���� ���������
                    yield float(number) if number != '.' else '.'
                    number = ''
                if function:  # ���������� �������, ���� ���� ���������
                    yield function
                    function = ''
                yield op  # ���������� �������� �������, ����� �� ��� ��������
                op = ''
            else:  # ���� �������� ���������
                if op:  # ���� ��� �������� �� ���������� ���� - ����������, ��������
                    yield op
                    op = ''
                if number:  # ���������� �����, ���� ���� ���������
                    yield float(number) if number != '.' else '.'
                    number = ''
                if function:  # ���������� �������, ���� ���� ���������
                    yield function
                    function = ''
                yield el  # ������������ ��������� ��������
            if number:  # ���������� �����, ���� ���� ���������
                yield float(number) if number != '.' else '.'
                number = ''
            if function:  # ���������� �������, ���� ���� ���������
                yield function
                function = ''
        elif el in PARENTHESES + (',',):  # ��������� ������ � ������� (���� ������� � ����������� �����������)
            if number:  # ���������� �����, ���� ���� ���������
                yield float(number) if number != '.' else '.'
                number = ''
            if function:  # ���������� �������, ���� ���� ���������
                yield function
                function = ''
            if op:  # ���������� ��������, ���� ��� ��������
                yield op
                op = ''
            yield el  # ���������� ������ ��� �������, ��� ������ ���������
    if function:  # ���������� �������, ���� ���� ���������
        yield function
    if number:  # ���������� �����, ���� ���� ���������
        yield float(number) if number != '.' else '.'
    if op:  # ���������� ��������, ���� ���� ���������
        yield op


def validate_parsed_list(parsed_list):
    if parsed_list[-1] in OPERATORS:
        raise ValueError('Operator at the end of the formula: "{}" '.format(parsed_list[-1]))
    if parsed_list[0] in BINARY_OPERATORS:
        raise ValueError('Formula can not start with binary operator "{}"'.format(parsed_list[0]))

    counter = 0  # counter for parentheses

    previous_el = ''
    for el in parsed_list:
        counter = matched_parentheses(el, counter)

        message = 'After {} element {} is forbidden!'.format(str(previous_el), str(el))

        if el == '.':
            raise ValueError('Single delimiter is prohibited in formula!')

        if isinstance(el, str) and el[0] in LETTERS:
            if el.lower() not in ALL_FUNCTIONS_AND_CONSTS:
                raise ValueError('Function or constant {} is not supported by calculator'.format(el))

        if previous_el == '(':
            if el in ((')', ',',) + tuple(BINARY_OPERATORS.keys())):
                raise ValueError(message)

        if previous_el == ')':
            if el in (('(',) + ALL_FUNCTIONS_AND_CONSTS) or isinstance(el, float):
                raise ValueError(message)

        if previous_el == ',':
            if el in (')', ',', '.'):
                raise ValueError(message)

        if previous_el in UNARY_OPERATORS:
            if el in ((')', ',',) + tuple(BINARY_OPERATORS.keys())):
                raise ValueError(message)

        if previous_el in BINARY_OPERATORS:
            if el in ((')', ',',) + tuple(BINARY_OPERATORS.keys())):
                raise ValueError(message)

        if previous_el in ALL_FUNCTIONS:
            if el != '(':
                raise ValueError(message)

        if isinstance(previous_el, float) or previous_el in MATH_CONSTS:
            if el in (('(',) + ALL_FUNCTIONS_AND_CONSTS) or isinstance(el, float):
                raise ValueError(message)

        previous_el = el

    if counter != 0:
        raise ValueError('Wrong number of opened or closed parentheses in formula!')

    return 'Formula was validated! Errors were not found.'


def sort_to_polish(parsed_formula):
    stack = []  # � �������� ����� ���������� ������
    previous_token = ''
    for token in parsed_formula:
        # ���� ������� - ��������, �� ���������� ������ ��� ��������� �� �����,
        # ��� ��������� ������ ��� ����� ����������,
        # �� ����������� ������ ��� ����������� �����.
        # ����� �� ���������� ���, ��� ��� ��������� �����-������������
        if token in ALL_FUNCTIONS_AND_OPERATORS_DICT:
            if token == '-' and previous_token in ('(', ',', '') + tuple(BINARY_OPERATORS.keys()):
                yield 0.0
                stack.append(token)
            else:
                while (stack and stack[-1] != "(" and
                       ALL_FUNCTIONS_AND_OPERATORS_DICT[token][0] <= ALL_FUNCTIONS_AND_OPERATORS_DICT[stack[-1]][0] and
                       token != '^'):
                    yield stack.pop()
                stack.append(token)
        elif token == ")":
            # ���� ������� - ����������� ������, ����� ��� �������� �� �����, �� ����������� ������,
            # � ����������� ������ ���������� �� �����.
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                yield x
        elif token == "(":
            # ���� ������� - ����������� ������, ������ ������� � � ����
            stack.append(token)
        elif token == ",":  # ����� ���������
            # ����� ��� ��������� �� ����� �� ����������� ������
            while stack and stack[-1] != "(":
                yield stack.pop()
            yield token
        else:
            # ���� ������� - ����� ��� ���������, �������� ��� ����� �� �����
            yield token
        previous_token = token
    while stack:
        yield stack.pop()


# TODO gcd only integer input
# TODO ldexp float + integer input
# TODO 1 arg, 2 args, 4 args - seems is working
def calc(polish_list):
    stack = []

    for token in polish_list:
        if token in MATH_FUNCTIONS:
            arguments = []
            func_name = getattr(math, token)

            #  TODO ���� ������� � ���
            if func_name != math.log:
                number_of_args = len(inspect.getfullargspec(func_name).args)
                for i in range(number_of_args):
                    if stack:
                        arguments.insert(0, stack.pop())
            else:
                # � � log ����� ���������� ���-�� ���������� ��������� ���������
                index_current_log_token = polish_list.index(token)
                try:
                    next_token_after_log = polish_list[index_current_log_token + 1]
                except IndexError:
                    next_token_after_log = ''

                if next_token_after_log in OPERATORS and len(stack) == 2:
                    arguments.insert(0, stack.pop())
                else:
                    if len(stack) >= 2:
                        arguments.insert(0, stack.pop())
                        arguments.insert(0, stack.pop())
                    else:
                        arguments.insert(0, stack.pop())

            try:
                function_result = func_name(*tuple(arguments))
            except TypeError:
                raise ValueError('Formula contains incorrect number of arguments in function.')

            stack.append(function_result)  # ��������� ��������, ���������� � ����
            arguments = []

        elif token in BUILT_IN_FUNCTIONS:
            x = stack.pop()  # �������� 1 ����o �� �����
            # TODO how to get built-in attr automatically
            if token == 'abs':
                stack.append(abs(x))
            elif token == 'round':
                stack.append(round(x))
        elif token in OPERATORS:  # ���� ���������� ������� - ��������,
            y, x = stack.pop(), stack.pop()  # �������� 2 ����� �� �����
            stack.append(OPERATORS[token][1](x, y))  # ��������� ��������, ���������� � ����
        elif token in MATH_CONSTS:
            stack.append(getattr(math, token))
        else:
            stack.append(token)

    if len(stack) > 1:
        raise ValueError('Formula contains incorrect number of arguments in function.')

    return stack[0]  # ��������� ���������� - ������������ ������� � �����


def process_unary_operations(validated_list):
    """
    :param validated_list: list of tokens after parsing of input formula and validation of it
    :return: processed_list: all unary '+' are removed, all redundant unary '-' are removed
    """
    stack_str = ''
    processed_list = []
    for el in validated_list:
        if el in UNARY_OPERATORS:
            stack_str += el
        else:
            is_unary_plus = ((processed_list and processed_list[-1] in (('(', ',') + tuple(BINARY_OPERATORS.keys()))) or
                             not processed_list)
            if stack_str:
                if '-' in stack_str:
                    if stack_str.count('-') % 2 == 0:  # ������� ���-�� -, ������� �� + ���� �� -
                        if is_unary_plus:
                            stack_str = ''
                        else:
                            stack_str = '+'
                    else:
                        stack_str = '-'
                else:
                    if is_unary_plus:
                        stack_str = ''
                    else:
                        stack_str = '+'
                if stack_str:
                    processed_list.append(stack_str)
                stack_str = ''
            processed_list.append(el)
    return processed_list


l = []
for el in sort_to_polish([1.0, '+', 2.0, '+', 3.0, '+', 'log', '(', 4.0, ',', 5.0, ')']):
    l.append(el)

print(l)
