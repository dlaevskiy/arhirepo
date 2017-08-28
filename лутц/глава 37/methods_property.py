class Person(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # name = property(name)
        "name property docs"
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):  # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self):  # name = name.deleter(name)
        print('remove...')
        del self._name


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)
