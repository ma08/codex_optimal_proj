from itertools import combinations

n = int(input())  # number of sticks
l = sorted(list(map(int, input().split())))  # list of stick lengths

count = 0
for i in combinations(l, 3):
    if i[0] + i[1] > i[2]:
        count += 1

print(count)
