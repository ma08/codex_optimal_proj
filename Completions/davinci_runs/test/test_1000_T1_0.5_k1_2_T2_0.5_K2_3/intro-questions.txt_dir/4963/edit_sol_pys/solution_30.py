n = int(input())
d = list(map(int, input().split()))

lineup = [0] * (n+1)

for i in range(1, n+1):
    lineup[d[i-1]] = i

print(*lineup)
