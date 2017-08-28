# 2.5. Searching and Replacing Text
# Problem
# You want to search for and replace a text pattern in a string.

# For simple literal patterns, use the str.replace()
text = 'yeah, but no, but yeah, but no, but yeah'

print text.replace('yeah', 'yeap')

# For more complicated patterns, use the sub() (re module)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re

newtext = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

print newtext

# For more complicated substitutions, its possible to specify a substitution callback function instead
from calendar import month_abbr

datepattern = re.compile(r'(\d+)/(\d+)/(\d+)')

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print datepattern.sub(change_date, text)
