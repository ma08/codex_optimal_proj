

import sys

b, d, c, l = map(int, sys.stdin.readline().split())  # read input
# check if input is valid

if l % 2 != 0:
    print('impossible')
    sys.exit()  # terminate program if input is invalid

answers = []  # store all possible solutions
# iterate through all possible combinations

for birds in range(l // b + 1):
    for dogs in range(l // d + 1):
        for cats in range(l // c + 1):
            if birds * b + dogs * d + cats * c == l:
                answers.append([birds, dogs, cats])
# print answer if possible

if len(answers) == 0:
    print('impossible')
else:
    for answer in sorted(answers):
        print(*answer)
