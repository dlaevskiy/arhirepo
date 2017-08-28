# 2.11. Stripping Unwanted Characters from Strings
# Problem
# You want to strip unwanted characters, such as whitespace, from the beginning, end, or
# middle of a text string.

# Whitespace stripping
s = ' hello   world \n'
s.strip()
'hello world'
s.lstrip()
'hello world \n'
s.rstrip()

# stripping in the middle

s.replace(' ', '')
