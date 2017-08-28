# 1.20. Combining Multiple Mappings into a Single
# Mapping
# Problem
# You have multiple dictionaries or mappings that you want to logically combine into a
# single mapping to perform certain operations, such as looking up values or checking
# for the existence of keys.

# from collections import ChainMap  # python 3.3

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# c = ChainMap(a,b)
# print(c['x']) # Outputs 1 (from a)
# print(c['y']) # Outputs 2 (from b)
# print(c['z']) # Outputs 3 (from a)
