registry = []


def register(func):
    print('running register (%s)' % func)
    registry.append(func)
    return func


@register
def func1():
    print('running func1()')


@register
def func2():
    print('running func2()')


def func3():
    print('running func3()')


def main():
    print('running main()')
    print('registry ->', registry)
    func1()
    func2()
    func3()
    print('registry ->', registry)


if __name__ == '__main__':
    main()
