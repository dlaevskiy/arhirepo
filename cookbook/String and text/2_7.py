# 2.7. Specifying a Regular Expression for the Shortest
# Match
# Problem
# You are trying to match a text pattern using regular expressions, but it is identifying the
# longest possible matches of a pattern. Instead, you would like to change it to find the
# shortest possible match.

import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print str_pat.findall(text1)  # ['no.']
text2 = 'Computer says "no." Phone says "yes."'
print str_pat.findall(text2)  # ['no." Phone says "yes.']

# To fix this, add the ? modifier after the * operator in the pattern, like this:
str_pat = re.compile(r'\"(.*?)\"')
print str_pat.findall(text2)  # ['no.', 'yes.']
