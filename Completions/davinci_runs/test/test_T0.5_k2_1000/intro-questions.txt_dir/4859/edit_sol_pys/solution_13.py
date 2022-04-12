
import sys

b, d, c, l = map(int, sys.stdin.readline().split())  # b - birds, d - dogs, c - cats, l - length of the fence,
# map(int, sys.stdin.readline().split()) - read input from console and split it by spaces

if l % 2 != 0:  # if the length of the fence is odd, it is impossible to make a fence
    print('impossible')
    sys.exit()

answers = []

for birds in range(l // b + 1):
    for dogs in range(l // d + 1):
        for cats in range(l // c + 1):
            if birds * b + dogs * d + cats * c == l:
                answers.append([birds, dogs, cats])

if len(answers) == 0:
    print('impossible')
else:
    for answer in sorted(answers):
        print(*answer)
