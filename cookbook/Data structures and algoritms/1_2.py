# 1.2. Unpacking Elements from Iterables of Arbitrary Length
# Problem
# You need to unpack N elements from an iterable, but the iterable may be longer than N
# elements, causing a 'too many values to unpack' exception.

# def drop_first_last(grades):
#     first, *middle, last = grades  # python 3
#     return avg(middle)  # python 3

# record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# name, email, *phone_numbers = user_record  # python 3
#
# print name

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

# for tag, *args in records:  # python 3
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
