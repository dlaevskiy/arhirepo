# 1.10. Removing Duplicates from a Sequence while >>Maintaining<< Order
# Problem
# You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items.


# for hashanable types aka list and etc
def dedupe_hash(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]

print list(dedupe_hash(a))

# for not hashanable types aka dict and etc
def dedupe_dict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

print list(dedupe_dict(b, key=lambda d: (d['x'], d['y'])))
