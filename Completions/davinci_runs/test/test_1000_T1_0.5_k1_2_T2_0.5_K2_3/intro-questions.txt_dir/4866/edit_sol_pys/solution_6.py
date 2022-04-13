import sys

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sys.stdout.write(str(a))
    sys.stdout.write('\n')
