
INF = 10**9
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])
ans = INF
for i in range(n):
    for j in range(n):
        if i != j:
            ans = min(ans, abs(stores[i][0] - stores[j][0]) + abs(stores[i][1] - stores[j][1]))
#-----Solve-----

print(ans)
#-----Display-----
