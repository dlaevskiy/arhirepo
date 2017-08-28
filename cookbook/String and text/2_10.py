# 2.10. Working with Unicode Characters in Regular
# Expressions
# Problem
# You are using regular expressions to process text, but are concerned about the handling
# of Unicode characters.

import re

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# Mixing Unicode and regular expressions is often a good way to make your head explode.
# If you are going to do it seriously, you should consider installing the third-party regex
# library, which provides full support for Unicode case folding, as well as a variety of other
# interesting features, including approximate matching
