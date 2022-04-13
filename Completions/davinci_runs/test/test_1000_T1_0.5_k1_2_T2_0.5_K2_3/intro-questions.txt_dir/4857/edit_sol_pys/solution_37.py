
from itertools import combinations_with_replacement

w, l = map(int, input().split())

letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(1, 27):
    if i * l == w:
        print(letters[i - 1] * l)
        break
    elif i * l > w:
        poss = []
        for j in range(i - 1, 0, -1):
            for com in combinations_with_replacement(letters[j - 1], l):
                if sum(com) == w:
                    poss.append(com)
        if len(poss) > 0:
            print(''.join(poss[0]))
            break
        else:
            print('impossible')
            break
