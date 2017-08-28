# 2.3. Matching Strings Using Shell Wildcard Patterns
# Problem
# You want to match text using the same wildcard patterns as are commonly used when
# working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

from fnmatch import fnmatch, fnmatchcase

print fnmatch('foo.txt', '*.txt')
print fnmatch('foo.txt', '?oo.txt')
print fnmatch('Dat45.csv', 'Dat[0-9]*')

# On OS X (Mac) the result will be false
print fnmatch('foo.txt', '*.TXT')

# On Windows the result will be true
print fnmatch('foo.txt', '*.TXT')

# If this distinction matters, use fnmatchcase() instead. It matches exactly based on the
# lower- and uppercase conventions that you supply:
print fnmatchcase('foo.txt', '*.TXT')

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print [addr for addr in addresses if fnmatchcase(addr, '* ST')]
