# 2.4. Matching and Searching for Text Patterns
# Problem
# You want to match or search text for a specific pattern.

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print text == 'yeah'  # False

# Search for the location of the first occurrence
print text.find('no')  # 10

# regular expressions
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1):
    print 'yes'
else:
    print 'no'

# If you are going to perform a lot of matches using the same pattern, it usually pays to
# precompile the regular expression pattern into a pattern object first.

datepattern = re.compile(r'\d+/\d+/\d+')

if datepattern.match(text1):
    print 'yes'
else:
    print 'no'

#groups
datepattern = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepattern.match('11/27/2012')

print m.group(0)
print m.group(1)
print m.group(2)
print m.groups()

month, day, year = m.groups()

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

print datepattern.findall(text)
