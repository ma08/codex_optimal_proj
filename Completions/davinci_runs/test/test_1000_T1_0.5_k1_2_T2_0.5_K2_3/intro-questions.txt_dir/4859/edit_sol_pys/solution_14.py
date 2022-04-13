
import sys

b, d, c, n = map(int, sys.stdin.readline().split())

if n % 2 != 0:
    print('impossible')
    sys.exit()

answers = []

for birds in range(n // b + 1):
    for dogs in range(n // d + 1):
        for cats in range(n // c + 1):
            if birds * b + dogs * d + cats * c == n:
                answers.append([birds, dogs, cats])

if len(answers) == 0:
    print('impossible')
else:
    for answer in sorted(answers):
        print(*answer)
