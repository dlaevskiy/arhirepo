class Indexer1(object):
    data = [1, 2, 3, 4]

    def __getitem__(self, index):
        return index ** 2

    def __setitem__(self, index, value):
        self.data[index] = value

class Indexer2(object):
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print 'getitem::', index
        return self.data[index]

class Stepper():
    data = 'Spam'

    def __getitem__(self, item):
        return self.data[item]

if __name__ == '__main__':
    X = Indexer1()
    print X[2]
    X[0] = 'hi'
    print X.data
    print '------------'
    Y = Indexer2()
    print Y[0]
    print Y[2:4]
    print '------------'
    Z = Stepper()
    print Z[1]
    for item in Z:  # for is calling __getitem__
        print item, ' '




