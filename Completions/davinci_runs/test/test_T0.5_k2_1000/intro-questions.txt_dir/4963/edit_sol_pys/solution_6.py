n = int(input())
d = list(map(int, input().split()))

lineup = [0] * n

for i in range(1, n):
    lineup[d[i-1]] = i

print(*lineup)
