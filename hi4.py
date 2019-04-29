# -*- coding: Windows-1251 -*-

import math
import string
import re

# TODO named tuple?
# TODO: to clarify priorities
OPERATORS = {'+': (1, lambda x, y: x + y),
             '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y),
             '/': (2, lambda x, y: x / y),
             # '//': (2, lambda x, y: x // y),
             # '%': (2, lambda x, y: x % y),
             # '^': (2, lambda x, y: x ^ y),
             # '<': (2, lambda x, y: x < y),
             # '<=': (2, lambda x, y: x <= y),
             # '>': (2, lambda x, y: x > y),
             # '>=': (2, lambda x, y: x >= y),
             # '==': (2, lambda x, y: x == y),
             # '!=': (2, lambda x, y: x != y),
             }

ADD_OPERATORS = ('(', ')')  # additional operators

DOUBLE_OPER_PART1 = ('/', '<', '>', '=', '!',)
DOUBLE_OPER_PART2 = ('/', '=',)


# TODO how to parse comlplicated functions like sin(sin(0.3))
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
            if elem != ')':  # try to find the end of the function
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
            # else:
            #     raise ValueError('Incorrect symbol in formula: {}!'.format(elem)) # TODO to think how process incorrect symbols
    if number:  # ���� � ����� ������ ���� �����, ����� ���
        yield float(number)
    if operator:
        raise ValueError('Incorrect formula: operator at the end of the formula!')


# L = []
# for elem in parse('1+sin(0.3)'):
#     L.append(elem)
#
# print L


# calculation of the functions

def calc_functions_in_list(parsed_list):
    new_L = []
    for elem in parsed_list:
        if isinstance(elem, str) and '(' in elem and ')' in elem:
            parse_function = re.split('\(|\)', elem)
            function_name = parse_function[0]
            function_argument = parse_function[1]
            try:
                value_of_function = getattr(math, function_name)(float(function_argument))
                new_L.append(value_of_function)
            except AttributeError:
                raise ValueError('Error in formula_string! Function: {} is not exist in library math!'.format(function_name))
            except ValueError:
                raise ValueError('Error in formula_string! Incorrect argument in function {}(): {}!'.format(function_name,
                                                                                                            function_argument))
        else:
            new_L.append(elem)
    return new_L


# [7.0, '*', 5.5, '+', 3.0]
def shunting_yard(parsed_formula):
    stack = []  # � �������� ����� ���������� ������
    for token in parsed_formula:
        # ���� ������� - ��������, �� ���������� ������ ��� ��������� �� �����,
        # ��� ��������� ������ ��� ����� ����������,
        # �� ����������� ������ ��� ����������� �����.
        # ����� �� ���������� ���, ��� ��� ��������� �����-������������
        if token in OPERATORS:
            while stack:
                prior_current_oper = OPERATORS[token][0]
                prior_last_stack_oper = OPERATORS[stack[-1]][0]
                if stack[-1] != "(" and prior_current_oper <= prior_last_stack_oper:
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


# L = []
# for elem in shunting_yard([7.0, '*', 5.5, '+', 3.0]):
#     L.append(elem)
#
# print L


def calc(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:  # ���� ���������� ������� - ��������,
            y, x = stack.pop(), stack.pop()  # �������� 2 ����� �� �����
            stack.append(OPERATORS[token][1](x, y))  # ��������� ��������, ���������� � ����
        else:
            stack.append(token)
    return stack[0]  # ��������� ���������� - ������������ ������� � �����


parsed_list = []
for element in parse('1+2*3'):
    parsed_list.append(element)
print parsed_list

calculated_list = []
for element in calc_functions_in_list(parsed_list):
    calculated_list.append(element)
print calculated_list

polish_list = []
for element in shunting_yard(calculated_list):
    polish_list.append(element)
print polish_list

result = calc(polish_list)

print result
