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
             }

PARENTHESES = ('(', ')')

DOUBLE_OPER_PART1 = ('/', '<', '>', '=', '!',)
DOUBLE_OPER_PART2 = ('/', '=',)

BUILT_IN_FUNCTIONS = ('abs', 'round')
MATH_FUNCTIONS = tuple([func for func in dir(math) if not func.startswith('_')])
ALL_FUNCTIONS = BUILT_IN_FUNCTIONS + MATH_FUNCTIONS


ALL_OPERATORS = tuple(OPERATORS.keys())
ALLOWED_TOKENS = ALL_OPERATORS + tuple(string.letters) + tuple(string.digits) + PARENTHESES + ('.',)


value = '1=>2'


# TODO how to parse complicated functions like sin(sin(0.3))
def parse(formula_string):
    number = ''
    operator_ = ''
    function = ''
    is_function = False
    for el in formula_string.strip():
        # finding function
        if el in string.ascii_lowercase or is_function is True:
            is_function = True
            if el != ')':  # try to find the end of the name of the math function
                function += el
            else:
                function += el  # to add ')' at the end of the function
                yield function
                function = ''
                is_function = False
        else:
            if el in string.digits + '.':  # если символ - цифра, то собираем число
                number += el
            elif number:  # если символ не цифра, то выдаём собранное число и начинаем собирать заново
                yield float(number)
                number = ''
            if el in OPERATORS or el in PARENTHESES or el in DOUBLE_OPER_PART1:
                if el in DOUBLE_OPER_PART1 and not operator_:
                    operator_ += el
                elif el in DOUBLE_OPER_PART2 and operator_:
                    operator_ += el
                    yield operator_
                    operator_ = ''
            elif el in PARENTHESES:
                yield el
    if number:  # если в конце строки есть число, выдаём его
        yield float(number)
    # if operator_:
    #     raise ValueError('Incorrect formula: operator at the end of the formula!')


parsed_list = []
for element in parse(value):
    parsed_list.append(element)
print('Parsed list is: >> {}'.format(parsed_list))


def validate_parsed_list(parsed_list):
    if not parsed_list:
        raise ValueError('Formula can not be empty!')
    if parsed_list[-1] in ALL_OPERATORS:
        raise ValueError('Operator at the end of the formula: "{}" '.format(parsed_list[-1]))
    COUNT = 0  # counter for parentheses


# validate_parsed_list(parsed_list)


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
    stack = []  # в качестве стэка используем список
    for token in parsed_formula:
        # если элемент - оператор, то отправляем дальше все операторы из стека,
        # чей приоритет больше или равен пришедшему,
        # до открывающей скобки или опустошения стека.
        # здесь мы пользуемся тем, что все операторы право-ассоциативны
        if token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            # если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
            # а открывающую скобку выкидываем из стека.
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                yield x
        elif token == "(":
            # если элемент - открывающая скобка, просто положим её в стек
            stack.append(token)
        else:
            # если элемент - число, отправим его сразу на выход
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
        if token in OPERATORS:  # если приходящий элемент - оператор,
            try:
                y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
                stack.append(OPERATORS[token][1](x, y))  # вычисляем оператор, возвращаем в стек
            except IndexError:
                raise ValueError('Incorrect formula! {}'.format(value))
        else:
            stack.append(token)
    return stack[0]  # результат вычисления - единственный элемент в стеке


result = calc(polish_list)

print('Result is: >> {}'.format(result))

