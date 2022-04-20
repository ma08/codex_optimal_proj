

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

if n <= 2:
    print 0
elif n == 3:
    if arr[1] - arr[0] == arr[2] - arr[1]:
        print 0
    else:
        print -1
else:
    d1 = arr[1] - arr[0]
    d2 = arr[2] - arr[1]
    if d1 == d2:
        print 0
    else:
        if arr[3] - arr[2] == d1:
            print 1
        elif arr[3] - arr[2] == d2:
            print 1
        else:
            print -1