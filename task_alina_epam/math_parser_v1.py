# -*- coding: Windows-1251 -*-

import math
import string
import operator

LETTERS = tuple(string.ascii_lowercase + string.ascii_uppercase)

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
MATH_FUNCTIONS = tuple([func for func in dir(math) if not func.startswith('_') and func not in ('e', 'pi')])
MATH_CONSTS = ('e', 'pi')

ALL_FUNCTIONS = BUILT_IN_FUNCTIONS + MATH_FUNCTIONS
ALL_FUNCTIONS_AND_CONSTS = MATH_FUNCTIONS + MATH_CONSTS

ALL_DIGITS = tuple(string.digits)

ALL_OPERATORS = tuple(OPERATORS.keys())
ALLOWED_TOKENS = OPERATORS_BEGIN + LETTERS + tuple(string.digits) + PARENTHESES + ('.', ',', ' ')


value = '3+1'


def matched_parentheses(el, count):
    if el == "(":
        count += 1
    elif el == ")":
        count -= 1
    return count


# TODO what if ['.*4.0']
def parse(formula_string):
    number = ''  # ��� ���������� �����
    op = ''  # ��� ���������� ����������
    function = ''  # ��� ���������� �������
    for el in formula_string.strip():
        if el not in ALLOWED_TOKENS:  # ��������� ����������� �� ������� � �������, ������ ��� ��� ������������
            raise ValueError('Formula contains incorrect symbol "{}"'.format(el))
        if el in LETTERS:  # ��������� �������
            function += el.lower()
            if op:  # ���������� ��������, ���� ��� ��������
                yield op
                op = ''
            if number:  # ���������� �����, ���� ���� ���������
                yield float(number)
                number = ''
        elif el in string.digits + '.':  # ��������� ����� ����� � � ������
            if function == 'log' and el == '1':  # ��� ������������ log10 � log1p
                function += el
            elif function == 'log1' and el == '0':  # ��� ������������ log10
                function += el
            else:
                if number.count('.') <= 1:  # ���������, ��� ����� �������� �� ����� ������ �����������
                    number += el
                else:
                    raise ValueError('Number can not contain more than one delimiter!')
                if op:  # ���������� ��������, ���� ��� ��������
                    yield op
                    op = ''
                if function:   # ���������� �������, ���� ���� ���������
                    yield function
                    function = ''
        elif el in OPERATORS_BEGIN:  # ��������� ����������
            if el in DOUBLE_OPER_PART1 and not op:  # ���� �������� ������� ��������, �������� � ���
                op += el
            elif el in DOUBLE_OPER_PART2 and op:  # ������ �������
                op += el
                if number:  # ���������� �����, ���� ���� ���������
                    yield float(number)
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
                    yield float(number)
                    number = ''
                if function:  # ���������� �������, ���� ���� ���������
                    yield function
                    function = ''
                yield el  # ������������ ��������� ��������
            if number:  # ���������� �����, ���� ���� ���������
                yield float(number)
                number = ''
            if function:  # ���������� �������, ���� ���� ���������
                yield function
                function = ''
        elif el in PARENTHESES + (',', ):  # ��������� ������ � ������� (���� ������� � ����������� �����������)
            if number:  # ���������� �����, ���� ���� ���������
                yield float(number)
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
        yield float(number)
    if op:  # ���������� ��������, ���� ���� ���������
        yield op


parsed_list = []
for element in parse(value):
    parsed_list.append(element)
print('Parsed list is: >> {}'.format(parsed_list))


# TODO how to process pow(2, 3, 4) - incorrect number of arguments
def validate_parsed_list(parsed_list):
    if not parsed_list:
        raise ValueError('Formula can not be empty!')
    if parsed_list[-1] in ALL_OPERATORS:
        raise ValueError('Operator at the end of the formula: "{}" '.format(parsed_list[-1]))
    if parsed_list[0] in BINARY_OPERATORS:
        raise ValueError('Formula can not start with binary operator "{}"'.format(parsed_list[0]))

    counter = 0  # counter for parentheses

    previous_el = ''
    for el in parsed_list:
        counter = matched_parentheses(el, counter)

        message = 'After {} element {} is forbidden!'.format(str(previous_el), str(el))

        if isinstance(el, str) and el[0] in LETTERS:
            if el.lower() not in ALL_FUNCTIONS_AND_CONSTS:
                raise ValueError(message)

        if previous_el == '(':
            if el in ((')', ',',) + tuple(BINARY_OPERATORS.keys())):
                raise ValueError(message)

        if previous_el == ')':
            if el in (('(', ',',) + ALL_FUNCTIONS_AND_CONSTS) or isinstance(el, float):
                raise ValueError(message)

        if previous_el == ',':
            if el in (('(', ')', ',',) + tuple(UNARY_OPERATORS.keys())):
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
            if el in (('(', ) + ALL_FUNCTIONS_AND_CONSTS) or isinstance(el, float):
                raise ValueError(message)

        previous_el = el

    if counter != 0:
        raise ValueError('Wrong number of opened or closed parentheses in formula!')

    return 'Formula was validated! Errors were not found.'


# TODO pi and e how to
# TODO more tnah one argument (,)
# TODO unari operation how to?
def sort_to_polish(parsed_formula):
    stack = []  # � �������� ����� ���������� ������
    for token in parsed_formula:
        # ���� ������� - ��������, �� ���������� ������ ��� ��������� �� �����,
        # ��� ��������� ������ ��� ����� ����������,
        # �� ����������� ������ ��� ����������� �����.
        # ����� �� ���������� ���, ��� ��� ��������� �����-������������
        if token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token in ALL_FUNCTIONS:
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
        else:
            # ���� ������� - ����� ��� ���������, �������� ��� ����� �� �����
            yield token
    while stack:
        yield stack.pop()


polish_list = []
for element in sort_to_polish(parsed_list):
    polish_list.append(element)
print('Polish list is: >> {}'.format(polish_list))


def calc(polish_list):
    stack = []
    for token in polish_list:
        if token in ALL_FUNCTIONS:
            x = stack.pop()  # �������� 1 ����o �� �����
            stack.append(getattr(math, token)(x))  # ��������� ��������, ���������� � ����
        elif token in OPERATORS:  # ���� ���������� ������� - ��������,
            try:
                y, x = stack.pop(), stack.pop()  # �������� 2 ����� �� �����
                stack.append(OPERATORS[token][1](x, y))  # ��������� ��������, ���������� � ����
            except IndexError:
                raise ValueError('Incorrect formula! {}'.format(value))
        else:
            stack.append(token)
    return stack[0]  # ��������� ���������� - ������������ ������� � �����


# result = calc(polish_list)
#
# print math.sin(math.sin(1))+math.cos(12*math.sin(13))
#
# print('Result is: >> {}'.format(result))


