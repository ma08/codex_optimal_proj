# -----Solution-----

import sys
from collections import Counter

word = sys.stdin.readline().strip()
count = Counter(word)
odds = 0
for i in count.values():
    if i % 2 != 0:
        odds += 1
print(odds)
