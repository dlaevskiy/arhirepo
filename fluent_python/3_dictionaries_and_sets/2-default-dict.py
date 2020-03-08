import sys
import re

# 1 - when you do this: d[key] - > __getitem__
# 2 - if key is absent in d - > __getitem__ call __missing__

WORD_RE = re.compile('\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # --- bad style ---
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            # --- good style ---
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
