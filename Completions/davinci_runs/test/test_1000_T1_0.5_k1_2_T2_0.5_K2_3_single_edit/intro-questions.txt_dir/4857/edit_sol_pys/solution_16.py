from itertools import combinations_with_replacement

l, w = map(int, input().split())

letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(1, 26):
    if i * l == w:
        print(letters[i - 1] * l)
        break
    elif i * l > w:
        poss = []
        for j in range(1, i):
            for com in combinations_with_replacement(letters[0:j], l):
                if sum(map(ord, com)) == w:
                    poss.append(''.join(com))
        if len(poss) > 0:
            print(poss[0])
            break
        else:
            print('impossible')
            break
