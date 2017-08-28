class Descriptor(object):
    def __get__(self, instance, owner):
        print self, instance, owner

class Subject(object):
    attr = Descriptor()

# X = Subject()
# print X.attr

#----------------------------------

class D(object):
    def __get__(*args):
        print('get')

    def __set__(self, instance, value):
        raise AttributeError('Cannot change attribute!')

class C(object):
    a = D()

X = C()
X.a
C.a
X.a = 99  # save value in X, switch off C.a
print X.a
print list(X.__dict__)

Y = C()
Y.a
C.a