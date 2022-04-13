

n = int(input())  # the number of adjacency relations
rel = list(map(int, input().split()))  # the adjacency relations

lineup = [0] * n  # the lineup

for i in range(1, n):
    lineup[rel[i-1]] = i

print(*lineup)
