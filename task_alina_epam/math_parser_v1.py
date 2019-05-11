# -*- coding: Windows-1251 -*-

import math
import string
import re
import operator


OPERATORS = {'+': (1, operator.add),
             '-': (1, operator.sub),
             '*': (2, operator.mul),
             '/': (2, operator.div),
             '//': (2, operator.floordiv),
             '%': (2, operator.imod),
             '^': (3, operator.ipow),
             '<': (0, operator.lt),
             '<=': (0, operator.le),
             '>': (0, operator.gt),
             '>=': (0, operator.ge),
             '==': (0, operator.eq),
             '!=': (0, operator.ne),
             'sin': (3, math.sin)
             }

ADD_OPERATORS = ('(', ')')  # additional operators

DOUBLE_OPER_PART1 = ('/', '<', '>', '=', '!',)
DOUBLE_OPER_PART2 = ('/', '=',)


# TODO how to parse complicated functions like sin(sin(0.3))
# TODO errors processing here?
def parse(formula_string):
    number = ''
    operator = ''
    function = ''
    is_function = False
    for elem in formula_string.strip():
        # 1. finding function
        if elem in string.ascii_lowercase or is_function is True:
            is_function = True
            if elem != ')':  # try to find the end of the name of the math function
                function += elem
            else:
                function += elem  # to add ')' at the end of the function
                yield function
                function = ''
                is_function = False
        else:
            if elem in string.digits + '.':  # ���� ������ - �����, �� �������� �����
                number += elem
            elif number:  # ���� ������ �� �����, �� ����� ��������� ����� � �������� �������� ������
                yield float(number)
                number = ''
            if elem in OPERATORS or elem in ADD_OPERATORS or elem in DOUBLE_OPER_PART1:
                if elem in DOUBLE_OPER_PART1 and not operator:
                    operator += elem
                elif elem in DOUBLE_OPER_PART2 and operator:
                    operator += elem
                    yield operator
                    operator = ''
                else:
                    yield elem
    if number:  # ���� � ����� ������ ���� �����, ����� ���
        yield float(number)
    if operator:
        raise ValueError('Incorrect formula: operator at the end of the formula!')


value = '1+sin(1+2)'

parsed_list = []
for element in parse(value):
    parsed_list.append(element)
print('Parsed list is: >> {}'.format(parsed_list))


def calc_functions_in_list(parsed_list):
    for elem in parsed_list:
        if isinstance(elem, str) and '(' in elem and ')' in elem:
            parse_function = re.split('\(|\)', elem)
            function_name = parse_function[0]
            function_argument = parse_function[1]
            try:
                if function_name == 'abs':
                    value_of_function = abs(float(function_argument))
                elif function_name == 'round':
                    value_of_function = round(float(function_argument))
                else:
                    value_of_function = getattr(math, function_name)(float(function_argument))
                yield value_of_function
            except AttributeError:
                raise ValueError('Error in formula_string! Function: {} is not exist in libraries!'.format(function_name))
            except ValueError:
                raise ValueError('Error in formula_string! Incorrect argument in function {}(): {}!'.format(function_name,
                                                                                                            function_argument))
        else:
            yield elem


calculated_list = []
for elem in calc_functions_in_list(parsed_list):
    calculated_list.append(elem)
print('Calculated list is: >> {}'.format(calculated_list))


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
            # ���� ������� - �����, �������� ��� ����� �� �����
            yield token
    while stack:
        yield stack.pop()


polish_list = []
for element in sort_to_polish(calculated_list):
    polish_list.append(element)
print('Polish list is: >> {}'.format(polish_list))


def calc(polish_list):
    stack = []
    for token in polish_list:
        if token in OPERATORS:  # ���� ���������� ������� - ��������,
            y, x = stack.pop(), stack.pop()  # �������� 2 ����� �� �����
            stack.append(OPERATORS[token][1](x, y))  # ��������� ��������, ���������� � ����
        else:
            stack.append(token)
    return stack[0]  # ��������� ���������� - ������������ ������� � �����


result = calc(polish_list)

print('Result is: >> {}'.format(result))

