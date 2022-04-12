from itertools import combinations

n, m = map(int, input().split())

l = list(map(int, input().split()))

poss = []

for i in range(1, len(l)):
    for com in combinations(l, i):
        if sum(com) == m:
            poss.append(com)

if len(poss) > 0:
    print(' '.join(map(str, poss[-1])))
else:
    print('impossible')
