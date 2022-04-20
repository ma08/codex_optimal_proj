

from collections import Counter
# input

n = int(input())
s = input()
# initialize counter

counter = 0

for i in Counter(s).values():
    counter += i - 1

print(counter)
