# -*- coding: Windows-1251 -*-

import math
import string
import operator


UNARY_OPERATORS = {'+': (1, operator.add),
                   '-': (1, operator.sub),
                   }

BINARY_OPERATORS = {'*': (2, operator.mul),
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
                    'sin': (3, math.sin),  # TODO remove it from here
                    'cos': (3, math.cos),
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

ALL_OPERATORS = tuple(OPERATORS.keys())
ALLOWED_TOKENS = OPERATORS_BEGIN + tuple(string.letters) + tuple(string.digits) + PARENTHESES + ('.', ',', ' ')


value = '2+13.0'


def matched_parentheses(el, count):
    if el == "(":
        count += 1
    elif el == ")":
        count -= 1
    return count


# TODO log10
# TODO log1p
# TODO how to parse functions with two arguments, were comma is present (leave comma?)
def parse(formula_string):
    number = ''
    op = ''
    function = ''
    for el in formula_string.strip():
        if el not in ALLOWED_TOKENS:
            raise ValueError('Formula contains incorrect symbol "{}"'.format(el))
        if el in string.letters:
            function += el.lower()
            if op:
                yield op
                op = ''
            if number:
                yield float(number)
                number = ''
        elif el in string.digits + '.':
            if function == 'log' and el == '1':
                function += el
            elif function == 'log1' and el == '0':
                function += el
            else:
                number += el
                if op:
                    yield op
                    op = ''
                if function:
                    yield function
                    function = ''
        elif el in OPERATORS_BEGIN:
            if el in DOUBLE_OPER_PART1 and not op:  # если возможен двойной оператор, добавили и ждём
                op += el
            elif el in DOUBLE_OPER_PART2 and op:  # найден двойной, добавили выстрелили обнулили
                op += el
                if number:  # выстрелили число, если было накоплено
                    yield float(number)
                    number = ''
                if function:  # выстрелили функцию, если было накоплено
                    yield function
                    function = ''
                yield op
                op = ''
            else:  # не двойной
                if op:  # если был накоплен на предыдущем шаге - выстрелили, обнулили
                    yield op
                    op = ''
                if number:  # выстрелили число, если было накоплено
                    yield float(number)
                    number = ''
                if function:  # выстрелили функцию, если было накоплено
                    yield function
                    function = ''
                yield el  # довыстрелили одинарный оператор
            if number:  # выстрелили число, если было накоплено
                yield float(number)
                number = ''
            if function:  # выстрелили функцию, если было накоплено
                yield function
                function = ''
        elif el in PARENTHESES + (',', ):
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


# TODO how to process pow(2, 3, 4) - incorrect number of arguments
def validate_parsed_list(parsed_list):
    if not parsed_list:
        raise ValueError('Formula can not be empty!')
    if parsed_list[-1] in ALL_OPERATORS:
        raise ValueError('Operator at the end of the formula: "{}" '.format(parsed_list[-1]))
    if parsed_list[0] in BINARY_OPERATORS:
        raise ValueError('Formula can not start with binary operator "{}"'.format(parsed_list[0]))
    counter = 0  # counter for parentheses
    was_number = False
    previous_el = ''
    for el in parsed_list:
        counter = matched_parentheses(el, counter)
        if el[0] in string.letters():
            if el.lower() not in ALL_FUNCTIONS_AND_CONSTS:
                raise ValueError('Formula contains incorrect function(s) or constant(s): {}'.format(el))
        if el[0] in OPERATORS:
            pass
        if isinstance(el, float) and was_number is False:
            was_number = True
        if el in BINARY_OPERATORS and previous_el in BINARY_OPERATORS:
            raise ValueError('Two or more binary operators in a row in formula!')
        previous_el = el
    if counter != 0:
        raise ValueError('Wrong number opened or closed parentheses in formula!')
    if was_number is False:
        raise ValueError('Formula does not contains numbers!')


# validate_parsed_list(parsed_list)

# TODO pi and e how to
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
        elif token in ALL_FUNCTIONS:  # TODO why here?
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
        if token in ALL_FUNCTIONS:
            x = stack.pop()  # забираем 1 числo из стека
            stack.append(getattr(math, token)(x))  # вычисляем оператор, возвращаем в стек
        elif token in OPERATORS:  # если приходящий элемент - оператор,
            try:
                y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
                stack.append(OPERATORS[token][1](x, y))  # вычисляем оператор, возвращаем в стек
            except IndexError:
                raise ValueError('Incorrect formula! {}'.format(value))
        else:
            stack.append(token)
    return stack[0]  # результат вычисления - единственный элемент в стеке


result = calc(polish_list)

print math.sin(math.sin(1))+math.cos(12*math.sin(13))

print('Result is: >> {}'.format(result))


