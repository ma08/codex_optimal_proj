

from collections import Counter

n = int(input())
s = input()

counter = 0


for i in Counter(s).values():
    counter += i - 1

print(counter)
