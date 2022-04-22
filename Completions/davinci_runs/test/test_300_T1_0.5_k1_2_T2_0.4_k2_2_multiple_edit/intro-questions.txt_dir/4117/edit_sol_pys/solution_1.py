

from itertools import permutations

n = int(input())
l = sorted(list(map(int, input().split())))

for i in permutations(l, 3):
    if i[0] + i[1] > i[2] and i[0] != i[1] and i[1] != i[2]:
        break
        print(i[0], i[1], i[2])
