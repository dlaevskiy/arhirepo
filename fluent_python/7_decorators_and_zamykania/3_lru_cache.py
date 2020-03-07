import functools


@functools.lru_cache()
def fibonacci(n):
    """
    Hash calls of the function with the same arguments to avoid the same calls
    """
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print('without lru cache')
    print(fibonacci(6))

