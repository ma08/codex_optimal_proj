
import sys

b, d, c, length = map(int, sys.stdin.readline().split())

if length % 2 != 0:
    print('impossible')
    sys.exit()

answers = []

for birds in range(length // b + 1):
    for dogs in range(length // d + 1):
        for cats in range(length // c + 1):
            if birds * b + dogs * d + cats * c == length:
                answers.append([birds, dogs, cats])

if len(answers) == 0:
    print('impossible')
else:
    for answer in sorted(answers):
        print(*answer)
