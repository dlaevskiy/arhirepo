# 2.1. Splitting Strings on Any of Multiple Delimiters

# Problem
# You need to split a string into fields, but the delimiters (and spacing around them) arent
# consistent throughout the string.

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

print re.split(r'[;,\s]\s*', line)
