

# -----Solution_1-----

from collections import Counter

word = input().strip()
count = Counter(word)
odds = 0
for i in count.values():
    if i % 2 != 0:
        odds += 1
print(odds)
