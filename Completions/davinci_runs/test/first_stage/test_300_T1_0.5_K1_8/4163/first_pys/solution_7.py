

import sys

N = int(sys.stdin.readline().rstrip())

count = 0

for i in range(N):
    dice = sys.stdin.readline().rstrip().split()
    if dice[0] == dice[1]:
        count += 1
    else:
        count = 0
    if count == 3:
        print("Yes")
        sys.exit()

print("No")