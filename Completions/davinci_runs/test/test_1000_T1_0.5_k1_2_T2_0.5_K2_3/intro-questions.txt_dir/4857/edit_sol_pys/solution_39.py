from itertools import combinations_with_replacement

l, w = map(int, input().split())

letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(1, 26):
    if i * l == w:
        print(letters[i - 1] * l)
        break
    elif i * l > w:
        poss = []
        for j in range(i - 1, 0, -1):
            for comb in combinations_with_replacement(letters[j - 1], l):
                if sum(comb) == w:
                    poss.append(comb)
        if len(poss) > 0:
            print(''.join(poss[0]))
            break
        else:
            print('impossible')
            break
