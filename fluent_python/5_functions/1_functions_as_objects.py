def factorial(n):
    """returns n"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

fact = factorial
print(fact)
print(fact(5))

iterator = map(factorial, range(11))
print(iterator)
print(list(iterator))

