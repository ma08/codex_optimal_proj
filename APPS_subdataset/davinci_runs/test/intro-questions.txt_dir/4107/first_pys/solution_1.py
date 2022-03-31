

import sys

n,k = map(int, sys.stdin.readline().split())

s = sys.stdin.readline().strip()

s = list(s)

s = [int(i) for i in s]

count = 0

for i in range(n):
    if s[i] == 1:
        s[max(0,i-k):min(n,i+k+1)] = [0] * len(s[max(0,i-k):min(n,i+k+1)])

for i in range(n):
    count += i * s[i]

print(count)