
import sys
b, d, c, l = map(int, sys.stdin.readline().split())  # b - birds, d - dogs, c - cats, l - length of the rope

if l % 2 != 0:  # if the length of the rope is odd, then it is impossible to tie the animals
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
