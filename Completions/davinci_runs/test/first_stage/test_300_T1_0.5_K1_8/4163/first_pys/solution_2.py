

import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    d1, d2 = map(int, sys.stdin.readline().rstrip().split())
    if d1 != d2:
        continue
    else:
        d1, d2 = map(int, sys.stdin.readline().rstrip().split())
        if d1 != d2:
            continue
        else:
            d1, d2 = map(int, sys.stdin.readline().rstrip().split())
            if d1 != d2:
                continue
            else:
                print("Yes")
                sys.exit()
print("No")