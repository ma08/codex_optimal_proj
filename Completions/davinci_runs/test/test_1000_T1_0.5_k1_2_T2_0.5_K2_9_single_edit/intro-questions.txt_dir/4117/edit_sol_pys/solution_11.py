
from itertools import combinations

n = int(input())
l = sorted(list(map(int, input().split())), reverse=True)

print(sum(1 for i in combinations(l, 3) if i[0] < i[1] + i[2]))
