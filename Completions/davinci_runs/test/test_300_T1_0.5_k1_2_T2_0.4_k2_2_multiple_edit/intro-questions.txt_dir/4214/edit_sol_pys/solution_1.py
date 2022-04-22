
import math

N = int(input())

towns = []
for i in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

def calc_permutation(lst):
    if len(lst) == 1:
        return [lst]
    permutation = []
    for i in range(len(lst)):
        tmp_lst = lst[:]
        tmp_lst.pop(i)
        for e in calc_permutation(tmp_lst):
            permutation.append([lst[i]] + e)
    return permutation

permutation = calc_permutation(list(range(1, N)))

total_dist = 0
for p in permutation:
    dist = 0
    prev = 0
    for i in p:
        dist += math.sqrt((towns[prev][0] - towns[i][0])**2 + (towns[prev][1] - towns[i][1])**2)
        prev = i
    dist += math.sqrt((towns[prev][0] - towns[0][0])**2 + (towns[prev][1] - towns[0][1])**2)
    total_dist += dist

print(total_dist / len(permutation))
