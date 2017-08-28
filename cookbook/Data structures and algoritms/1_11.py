# 1.11. Naming a Slice
# Problem
# Your program has become an unreadable mess of hardcoded slice indices and you want to clean it up

record = '0123456789012345678901234567890123456789012345678901234567890'

SHARES = slice(20, 32)
PRICE = slice(40, 48)

# instead of >> cost = int(record[20:32]) * float(record[40:48])

cost = int(record[SHARES]) * float(record[PRICE])

print cost

a = slice(10, 50, 2)  # creation of a slice object
print a.start, a.stop, a.step
print a.indices(5)
