
# https://codeforces.com/problemset/problem/1228/A

from collections import Counter

l, r = map(int, input().split())


counter = 0

for i in Counter(s).values():
    counter += i - 1

print(counter)
