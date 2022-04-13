

import sys

a, b, c, d = map(int, input().split())

if d % 2 != 0:
    print('impossible')
    sys.exit()

answers = []

for x in range(d // a + 1):
    for y in range(d // b + 1):
        for z in range(d // c + 1):
            if x * a + y * b + z * c == d:
                answers.append([x, y, z])

if len(answers) == 0:
    print('impossible')
else:
    for answer in sorted(answers):
        print(*answer)
