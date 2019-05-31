# -*- coding: Windows-1251 -*-
import sys
import math
import string
import operator
import inspect

from pip._vendor.msgpack.fallback import xrange

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
ALL_FUNCTIONS_AND_CONSTS = ALL_FUNCTIONS + MATH_CONSTS

ALL_FUNCTIONS_DICT = {el: (4,) for el in ALL_FUNCTIONS}
ALL_FUNCTIONS_AND_OPERATORS_DICT = ALL_FUNCTIONS_DICT.copy()
ALL_FUNCTIONS_AND_OPERATORS_DICT.update(OPERATORS)

ALL_DIGITS = tuple(string.digits)

ALL_OPERATORS = tuple(OPERATORS.keys())
ALLOWED_TOKENS = OPERATORS_BEGIN + LETTERS + tuple(string.digits) + PARENTHESES + ('.', ',', ' ')


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
    if '..' in formula_string:  # проверяем, что число содержит не более одного разделителя
        raise ValueError('Number can not contain more than one delimiter "." !')
    for el in formula_string.strip():
        if el not in ALLOWED_TOKENS:  # проверка на разрешённые элементы
            raise ValueError('Formula contains incorrect symbol "{}"'.format(el))


def parse(formula_string):
    number = ''  # для накопления чисел
    op = ''  # для накопления операторов
    function = ''  # для накопления функций
    for el in formula_string.strip():
        if el in LETTERS:  # обработка функции
            function += el.lower()
            if op:  # выстрелили оператор, если был накоплен
                yield op
                op = ''
            if number:  # выстрелили число, если было накоплено
                yield float(number) if number != '.' else '.'
                number = ''
        elif el in string.digits + '.':  # обработка чисел целых и с точкой
            if function:
                function += el  # продолжаем накапливать функцию, пока не встретим что-то отличное от цифры
            else:
                number += el
                if op:  # выстрелили оператор, если был накоплен
                    yield op
                    op = ''
                if function:  # выстрелили функцию, если было накоплено
                    yield function
                    function = ''
        elif el in OPERATORS_BEGIN:  # обработка операторов
            if el in DOUBLE_OPER_PART1 and not op:  # если возможен двойной оператор, добавили и ждём
                op += el
            elif el in DOUBLE_OPER_PART2 and op:  # найден двойной
                op += el
                if number:  # выстрелили число, если было накоплено
                    yield float(number) if number != '.' else '.'
                    number = ''
                if function:  # выстрелили функцию, если было накоплено
                    yield function
                    function = ''
                yield op  # выстрелили оператор двойной, когда он был накоплен
                op = ''
            else:  # если оператор одинарный
                if op:  # если был накоплен на предыдущем шаге - выстрелили, обнулили
                    yield op
                    op = ''
                if number:  # выстрелили число, если было накоплено
                    yield float(number) if number != '.' else '.'
                    number = ''
                if function:  # выстрелили функцию, если было накоплено
                    yield function
                    function = ''
                yield el  # довыстрелили одинарный оператор
            if number:  # выстрелили число, если было накоплено
                yield float(number) if number != '.' else '.'
                number = ''
            if function:  # выстрелили функцию, если было накоплено
                yield function
                function = ''
        elif el in PARENTHESES + (',',):  # обработка скобок и запятых (если функция с несколькими аргументами)
            if number:  # выстрелили число, если было накоплено
                yield float(number) if number != '.' else '.'
                number = ''
            if function:  # выстрелили функцию, если было накоплено
                yield function
                function = ''
            if op:  # выстрелили оператор, если был накоплен
                yield op
                op = ''
            yield el  # выстрелили скобку или запятую, как только встретили
    if function:  # выстрелили функцию, если было накоплено
        yield function
    if number:  # выстрелили число, если было накоплено
        yield float(number) if number != '.' else '.'
    if op:  # выстрелили оператор, если было накоплено
        yield op


# TODO how to process sin(2, 3) - incorrect number of arguments, allowed only one - in progress
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

        if el == '.':
            raise ValueError('Single delimiter is prohibited in formula!')

        if isinstance(el, str) and el[0] in LETTERS:
            if el.lower() not in ALL_FUNCTIONS_AND_CONSTS:
                raise ValueError(message)

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

    return 'Formula was validated! Errors were not found'


# TODO pi and e how to - seems is working
# TODO more that one argument (,) - seems is working
# TODO unari operation how to? - seems is working
def sort_to_polish(parsed_formula):
    stack = []  # в качестве стэка используем список
    previous_token = ''
    for token in parsed_formula:
        # если элемент - оператор, то отправляем дальше все операторы из стека,
        # чей приоритет больше или равен пришедшему,
        # до открывающей скобки или опустошения стека.
        # здесь мы пользуемся тем, что все операторы право-ассоциативны
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
        elif token == ",":  # конец аргумента
            # выдаём все операторы из стека до открывающей скобки
            while stack and stack[-1] != "(":
                yield stack.pop()
            yield token
        else:
            # если элемент - число или константа, отправим его сразу на выход
            yield token
        previous_token = token
    while stack:
        yield stack.pop()


# TODO fsum how
# TODO gcd only integer input
# TODO 1 arg, 2 args, 4 args
def calc(polish_list):
    stack = []
    for token in polish_list:
        if token in MATH_FUNCTIONS:
            func_name = getattr(math, token)
            number_arguments = len(inspect.getfullargspec(func_name).args)
            x = stack.pop()  # забираем 1 числo из стека
            stack.append(func_name(x))  # вычисляем оператор, возвращаем в стек
        elif token in BUILT_IN_FUNCTIONS:
            x = stack.pop()  # забираем 1 числo из стека
            if token == 'abs':
                stack.append(abs(x))
            elif token == 'round':
                stack.append(round(x))
        elif token in OPERATORS:  # если приходящий элемент - оператор,
            y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
            stack.append(OPERATORS[token][1](x, y))  # вычисляем оператор, возвращаем в стек
        elif token in MATH_CONSTS:
            stack.append(getattr(math, token))
        else:
            stack.append(token)
    return stack[0]  # результат вычисления - единственный элемент в стеке


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
                    if stack_str.count('-') % 2 == 0:  # считаем кол-во -, заменяя на + либо -
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


def check(num):
    L = []
    stack = [1, 2, 3, 4, 5]
    for i in range(num):
        L.append(stack.pop())
    return L


print(check(2))
# print([1, 2, 3, 4, 5].pop())

