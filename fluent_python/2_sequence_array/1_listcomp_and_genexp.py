# list comprehensive
import array

colors = ['black', 'white', ]
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# generators
symbols = '@#$%^7'
gen = tuple(ord(symbol) for symbol in symbols)
print(gen)

ar = array.array('I', (ord(symbol) for symbol in symbols))
print(ar)

# tuples

year, name = (1989, 'Dzmitry')
a, b, *rest = range(5)
print(a, b, *rest)

s = 'sdjhjkdhfodjsjfdjflkjdsouwijfhfdh'


def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

print(split_len(s, 10))

