class Number(object):
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

if __name__ == '__main__':
    X = Number(5)
    Y = X - 2
    print Y.data
