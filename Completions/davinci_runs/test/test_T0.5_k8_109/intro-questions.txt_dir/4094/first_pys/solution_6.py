

import sys

k = int(sys.stdin.readline())

if k % 2 == 0 or k % 5 == 0:
    print(-1)
else:
    n = 7
    i = 1
    while True:
        if n % k == 0:
            print(i)
            break
        else:
            i += 1
            n = n * 10 + 7