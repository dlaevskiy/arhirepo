# find shared elements in dicts

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# shared keys
print set(a.keys()) & set(b.keys())  # { 'x', 'y' }
# present only in a
# print a.keys() - b.keys()  # { 'z' }
# # shared pairs
# print a.items() & b.items()  # {('y', 2)}

