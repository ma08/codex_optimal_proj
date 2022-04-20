
from collections import Counter

n = int(input())
s = input()

counter = 0

for i in Counter(s).values():
    if i > 1:
        counter += i - 1

print(counter)
