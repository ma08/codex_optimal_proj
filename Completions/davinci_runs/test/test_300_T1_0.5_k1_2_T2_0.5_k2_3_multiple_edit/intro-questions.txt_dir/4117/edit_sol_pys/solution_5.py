from itertools import permutations

n = int(input())
l = list(map(int, input().split()))

l.sort()

for i in permutations(l, 3):
    if i[0] + i[1] > i[2] and i[1] + i[2] > i[0] and i[0] + i[2] > i[1]:
        print("YES")
        exit(0)
print("NO")
