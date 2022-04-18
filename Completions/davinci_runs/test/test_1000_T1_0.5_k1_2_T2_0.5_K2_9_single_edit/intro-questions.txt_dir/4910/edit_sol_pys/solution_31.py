

#import sys
#import math

#s = sys.stdin.readline()
#s = s.rstrip()
#s = s.split()

s = "10 ghost mummy witch demon demon demon demon demon demon demon" #input("Enter: ")

print(s)
s = s.split()

n = int(s[0])

print(s)
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
