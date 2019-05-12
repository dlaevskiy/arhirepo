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

# value_of_function = getattr(math, function_name)(float(function_argument))

def matched_parentheses(el, count):
    if el == "(":
        count += 1
    elif el == ")":
        count -= 1
    if count == 0:
        return True
    return False


# TODO how to parse complicated functions like sin(sin(0.3))
def parse(formula_string):
    number = ''
    op = ''
    function = ''
    for el in formula_string.strip():
        if el in string.letters:
            function += el
            if op:
                yield op
                op = ''
            if number:
                yield float(number)
                number = ''
        elif el in string.digits + '.':
            number += el
            if op:
                yield op
                op = ''
            if function:
                yield function
                function = ''
        elif el in OPERATORS or el in DOUBLE_OPER_PART1:
            op += el
            if number:
                yield float(number)
                number = ''
            if function:
                yield function
                function = ''
        elif el in PARENTHESES:
            if number:
                yield float(number)
                number = ''
            if function:
                yield function
                function = ''
            if op:
                yield op
                op = ''
            yield el
    if function:
        yield function
    if number:
        yield float(number)
    if op:
        yield op


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
for element in sort_to_polish(parsed_list):
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


# result = calc(polish_list)
#
# print('Result is: >> {}'.format(result))

