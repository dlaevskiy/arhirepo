# 1.6. Mapping Keys to Multiple Values in a Dictionary
# Problem
# You want to make a dictionary that maps keys to more than one value (a so-called multidict).

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)


f = defaultdict(set)
f['a'].add(1)
f['a'].add(2)
f['b'].add(4)


print d
print f

d = {}

d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print d

pairs = (1, 2)
# without default dict
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# with default dict - cleaner code
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
