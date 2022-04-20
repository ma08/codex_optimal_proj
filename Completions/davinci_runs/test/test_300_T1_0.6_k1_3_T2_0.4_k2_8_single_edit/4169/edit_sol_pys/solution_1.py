
INF = 10**10
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])
ans = 0
for i in range(m):
    minv = INF
    for j in range(n):
        minv = min(minv, stores[j][0] + i * stores[j][1])
    ans += minv
print(ans)
#-----Solve-----

#-----Display-----
