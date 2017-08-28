X = 11  # global name, attribute of module (X, example6-mynames.X)

def f():
    print X  # call global X

def g():
    X = 22  # local variable
    print X


class C(object):
    X = 33  # attribute of class (C.X)

    def m(self):
        X = 44  # local variable in method
        self.X = 55  # attribute of instance (instance.X)

if __name__ == '__main__':
    print X  # 11
    f()  # 11
    g()  # 22
    print X  # 11
    obj = C()
    print obj.X  # 33 (variable of class, inheritance of instance)
    obj.m()
    print obj.X  # 55
    print C.X  # 33
    # print(C.m.X) # error
    # print(g.X) # error
