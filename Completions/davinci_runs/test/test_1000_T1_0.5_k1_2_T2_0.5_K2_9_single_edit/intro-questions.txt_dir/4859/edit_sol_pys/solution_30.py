import sys

birds, dogs, cats, legs = map(int, sys.stdin.readline().split())

if legs % 2 != 0:
    print('impossible')
    sys.exit()

answers = []

for birds in range(legs // birds + 1):
    for dogs in range(legs // dogs + 1):
        for cats in range(legs // cats + 1):
            if birds * birds + dogs * dogs + cats * cats == legs:
                answers.append([birds, dogs, cats])

if len(answers) == 0:
    print('impossible')
else:
    for answer in sorted(answers):
        print(*answer)
