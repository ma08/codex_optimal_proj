import collections

n = int(input())
s = input()

counter = 0

for i in collections.Counter(s).values():
    counter += i - 1

print(counter)
