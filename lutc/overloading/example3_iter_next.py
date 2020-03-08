class Squares(object):
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):  # __next__ in Python 3.0
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

class SkipIterator(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipObject(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


if __name__ == '__main__':
    print 'test Squares class'
    for i in Squares(1, 5):
        print i
    print '-------'

    print 'test Skip classes'
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))

    for x in skipper:
        for y in skipper:
            print x + y

