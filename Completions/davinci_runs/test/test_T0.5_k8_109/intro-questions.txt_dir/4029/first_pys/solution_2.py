

import sys

n = sys.stdin.readline()[:-1]

moves = 0
while len(n) > 1:
    if int(n[-1]) % 5 == 0:
        moves += 1
        break

    if int(n[-2:]) % 25 == 0:
        moves += 1
        break

    if int(n[-1]) % 5 == 0:
        moves += 1
        break

    if n[-1] == '0':
        n = n[:-1]
        moves += 1
    else:
        n = n[:-2] + n[-1] + n[-2]
        moves += 1

if len(n) == 1:
    print(-1)
else:
    print(moves)