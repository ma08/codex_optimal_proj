
#
n = int(input())  # the number of adjacency relations
d = list(map(int, input().split()))  # the adjacency relations

lineup = [0] * n  # the lineup

for i in range(1, n):
    lineup[d[i-1]] = i

print(*lineup)
