#https://www.hackerrank.com/challenges/triangle-quest-2/problem

from itertools import combinations

for i in range(1, int(input())+1):
    print(((10**i)-1)**2//81)

count = 0
for i in combinations(l, 3):
    if i[0] + i[1] > i[2]:
        count += 1

print(count)
