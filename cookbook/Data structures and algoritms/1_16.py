# 1.16. Filtering Sequence Elements
# Problem
# You have data inside of a sequence, and need to extract values or reduce the sequence
# using some criteria.

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print [n for n in mylist if n > 0]

pos = (n for n in mylist if n > 0)  # if large can use generator

for x in pos:
    print x

# if wrong element in sequence
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print ivals

from itertools import compress

addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print more5

print list(compress(addresses, more5))
