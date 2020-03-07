def deco(func):
    def inner():
        func()
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


# target = deco(target)


target()


# zamykania
def make_averager_v1():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return print(total / len(series))

    return averager


avg = make_averager_v1()

# inspection of the avg
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

avg(10)
avg(11)
avg(12)


def make_averager_v2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total  # only for Python3
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager_v2()

# inspection of the avg
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

avg(10)
avg(11)
avg(12)
