# 1.18. Mapping Names to Sequence Elements
# Problem
# You have code that accesses list or tuple elements by position, but this makes the code
# somewhat difficult to read at times. You d also like to be less dependent on position in
# the structure, by accessing the elements by name.

# One possible use of a namedtuple is as a replacement for a dictionary, which requires
# more space to store. Thus, if you are building large data structures involving dictionaries,
# use of a namedtuple will be more efficient. However, be aware that unlike a dictionary,
# a namedtuple is immutable

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print sub

print sub.addr
print sub.joined


