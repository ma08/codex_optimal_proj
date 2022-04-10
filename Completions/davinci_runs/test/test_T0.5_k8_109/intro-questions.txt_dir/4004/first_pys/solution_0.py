

import sys

def solution():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if n == 1:
        print(0)
    elif n == 2 and a[0] == a[1]:
        print(0)
    elif n == 2 and a[0] != a[1]:
        print(a[1]-a[0])
    elif n > 2:
        if a[0] == a[1]:
            print(0)
        else:
            d = a[1]-a[0]
            for i in range(2,n):
                if a[i] - a[i-1] != d:
                    print(-1)
                    sys.exit()
            print(d)

solution()