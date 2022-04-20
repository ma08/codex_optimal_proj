
n,m = map(int,input().split())

books = []
for _ in range(n):
    books.append(list(map(int, input().split())))

x = list(map(int, input().split()))

ans = 10**9

for i in range(2**n):
    cost = 0
    algo = [0]*m
    for j in range(n):
        if(i >> j & 1):
            cost += books[j][0]
            for k in range(m):
                algo[k] += books[j][k+1]
    if(all(a >= x_i for a, x_i in zip(algo, x))):
        ans = min(ans, cost)

if(ans == 10**9):
    print(-1)
else:
    print(ans)
