import sys


n, c = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))

eaten = 0
curr = 0
w.sort()

for x in w:
    if curr + x <= c:
        curr += x
        eaten += 1

print(eaten)
