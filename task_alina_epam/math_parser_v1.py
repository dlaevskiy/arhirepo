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
             'sin': (0, lambda x: math.sin(x))
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
            if elem != '(':  # try to find the end of the name of the math function
                function += elem
            else:
                yield function
                yield '('
                function = ''
                is_function = False
        else:
            if elem in string.digits + '.':  # если символ - цифра, то собираем число
                number += elem
            elif number:  # если символ не цифра, то выдаём собранное число и начинаем собирать заново
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
    if number:  # если в конце строки есть число, выдаём его
        yield float(number)
    if operator:
        raise ValueError('Incorrect formula: operator at the end of the formula!')


parsed_list = []
for element in parse('1+5*4'):
    parsed_list.append(element)
print parsed_list


# [7.0, '*', 5.5, '+', 3.0]
def shunting_yard(parsed_formula):
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
for element in shunting_yard(parsed_list):
    polish_list.append(element)
print polish_list


def calc(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:  # если приходящий элемент - оператор,
            y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
            stack.append(OPERATORS[token][1](x, y))  # вычисляем оператор, возвращаем в стек
        else:
            stack.append(token)
    return stack[0]  # результат вычисления - единственный элемент в стеке


result = calc(polish_list)

print result
