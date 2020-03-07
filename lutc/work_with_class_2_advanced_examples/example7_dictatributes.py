class super(object):
    """
    Hi, this is doc of super class
    """
    def hello(self):
        self.data1 = 'spam'

class sub(super):
    def hola(self):
        self.data2 = 'eggs'


if __name__ == '__main__':
    X = sub()
    print X.__dict__  # dict names of instance
    print X.__class__  # name of class of instance
    print sub.__bases__  # super classes of this class
    Y = sub()
    X.hello()
    print X.__dict__
    print sub.__dict__.keys()
    print super.__dict__.keys()
    print Y.__dict__
    print super.__doc__
    print X.data1, X.__dict__['data1']  # two the same operations