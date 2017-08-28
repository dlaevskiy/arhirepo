# 2.9. Normalizing Unicode Text to a Standard
# Representation
# Problem
# You are working with Unicode strings, but need to make sure that all of the strings have
# the same underlying representation.

import unicodedata

s1 = u'Spicy Jalape\u00f1o'
s2 = u'Spicy Jalapen\u0303o'

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)

print t1 == t2
