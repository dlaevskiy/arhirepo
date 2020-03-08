import random


class BingoCage(object):

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


print(BingoCage('123456789'))
bingo = BingoCage('123456789')
print(bingo())
