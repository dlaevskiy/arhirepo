#method example

class NextClass(object):
    def printer(self, text):
        self.message = text
        print self.message


x = NextClass()

x.printer('instance call')

print x.message

NextClass.printer(x, 'class call')  # is equal to x.printer

print x.message
