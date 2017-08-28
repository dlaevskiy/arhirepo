# 1.12. Determining the Most Frequently Occurring Items in a Sequence

# Problem
# You have a sequence of items, and you would like to determine the most frequently occurring items in the sequence.

from collections import Counter

words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)

top = word_counts.most_common(3)

print top
print word_counts['eyes']

