# call init of super classes

class Supper(object):
    def __init__(self, x):
        self.x = x
        self.name = 'Name'

    def hi(self, text):
        print text

class Sub(Supper):
    def __init__(self, x, y):
        Supper.__init__(self, x)  # call init from super class
        self.x = x
        self.y = y

I = Sub(1, 2)

print I.x
print I.y
print I.hi('EEEEE')
