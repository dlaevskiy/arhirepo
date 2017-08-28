# 2.8. Writing a Regular Expression for Multiline Patterns
# Problem
# You are trying to match a block of text using a regular expression, but you need the match
# to span multiple lines.

import re

text2 = '''/* this is a
            multiline comment */
        '''


comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print comment.findall(text2)  # [' this is a\n multiline comment ']

# The re.compile() function accepts a flag, re.DOTALL, which is useful here

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print comment.findall(text2)
