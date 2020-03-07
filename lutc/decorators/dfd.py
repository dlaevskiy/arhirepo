import re

if re.match('\d{7,8}', '123456'):
    print 'hi'
else:
    print 'no'

