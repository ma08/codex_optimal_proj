import sys
while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    for i in range(n):
        print(a[i], end=" ")
    print()
