

N, T = map(int, input().split())

cost = []
for i in range(N):
    c, t = map(int, input().split())
    cost.append([c, t])

cost.sort(key=lambda x: x[0])

ans = "TLE"
for i in range(len(cost)):
    if cost[i][1] <= T:
        ans = cost[i][0]
        break

print(ans)