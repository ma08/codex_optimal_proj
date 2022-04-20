

import sys

N = int(sys.stdin.readline())
count = 0

for i in range(N):
    D = [int(x) for x in sys.stdin.readline().split()]
    if D[0] == D[1]:
        count += 1
    else:
        count = 0
    if count == 3:
        print("Yes")
        sys.exit()
print("No")