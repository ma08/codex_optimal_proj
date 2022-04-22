
from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    l = sorted(list(map(int, input().split())))

count = 0
for i in combinations(l, 3):
    if i[0] + i[1] > i[2]:
        count += 1

print(count)
