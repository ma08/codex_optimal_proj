
import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))[1:]

l.sort()

if l[-1] < sum(l[:-1]):
    print('Yes')
else:
    print('No')
