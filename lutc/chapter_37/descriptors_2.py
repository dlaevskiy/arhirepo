class Name(object):
    """name descriptor docs"""

    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete__(self, instance):
        print('remove...')
        del instance._name


class Person(object):
    def __init__(self, name):
        self._name = name

    name = Name()


bob = Person('Bob Smith')
print(bob.name)

bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)

sue = Person('Sue Jones')
print(sue.name)
print(Name.__doc__)
