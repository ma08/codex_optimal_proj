import sys

a = int(sys.stdin.readline())
for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    print(b[0]+b[1])
