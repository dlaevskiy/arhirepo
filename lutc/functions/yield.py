# generator

mygenerator = (x*x for x in range(3))

# for i in mygenerator:
#     print i

def createGenerator():
    """
    return generator object
    """
    mylist = range(3)
    for i in mylist:
        yield i * i

generator = createGenerator()

print generator

for j in generator:
    print j