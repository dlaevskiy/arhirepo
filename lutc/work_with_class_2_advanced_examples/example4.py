# princip rashirenia of a class with help of method from super class

class Supper(object):
    def method(self):
        print 'in Super.method'

class Sub(Supper):
    def method(self):
        print 'staring Sub.method'
        Supper.method(self)
        print 'ending Sub.method'

x = Sub()

x.method()

