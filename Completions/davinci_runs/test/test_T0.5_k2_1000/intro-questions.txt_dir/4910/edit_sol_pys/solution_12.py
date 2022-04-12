
import sys

s = sys.stdin.readline()
s = s.rstrip()
s = s.split()

n = int(s[0])
s = s[1:]

d = {}

for i in range(n):
    if s[i] not in d:
        d[s[i]] = 1
    else:
        d[s[i]] += 1

m = max(d.values())

for k, v in d.items():
    if v == m:
        print(k)
