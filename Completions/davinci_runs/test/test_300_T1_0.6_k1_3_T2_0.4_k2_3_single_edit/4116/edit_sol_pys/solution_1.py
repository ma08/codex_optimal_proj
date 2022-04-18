

import sys

N = int(sys.stdin.readline())

if N % 2 == 0 or N % 3 == 0 or N % 5 == 0 or N % 7 == 0 or N % 11 == 0 or N % 13 == 0 or N % 17 == 0 or N % 19 == 0:
    print("Yes")
else:
    print("No")
