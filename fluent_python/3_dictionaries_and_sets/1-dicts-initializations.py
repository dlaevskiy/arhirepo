a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'one': 1, 'two': 2, 'three': 3})
print(a == b == c == d == e)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India')
]

# dict comprehensive

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
