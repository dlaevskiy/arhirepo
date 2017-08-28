# 2.2. Matching Text at the Start or End of a String
# Problem
# You need to check the start or end of a string for specific text patterns, such as filename
# extensions, URL schemes, and so on.

filename = 'spam.txt'

print filename.endswith('.txt')
print filename.startswith('file:')
