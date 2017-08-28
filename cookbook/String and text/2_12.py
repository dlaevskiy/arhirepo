# 2.12. Sanitizing and Cleaning Up Text
# Problem
# Some bored script kiddie has entered the text p?t??? into a form on your web page
# and youd like to clean it up somehow.

s = 'p?t???\fis\tawesome\r\n'

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
    }

a = s.translate(remap)

# Yet another technique for cleaning up text involves I/O decoding and encoding functions
# The idea here is to first do some preliminary cleanup of the text, and then run it
# through a combination of encode() or decode() operations to strip or alter it.

import unicodedata

b = unicodedata.normalize('NFD', s)
b.encode('ascii', 'ignore').decode('ascii')

# replace is faster than translate
