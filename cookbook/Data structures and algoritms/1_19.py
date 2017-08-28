# 1.19. Transforming and Reducing Data at the Same Time
# Problem
# You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
# transform or filter the data.

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

print s

# Determine if any .py files exist in a directory
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print ','.join(str(x) for x in s)

