import sys
input = sys.stdin.readline

n,m = map(int,input().split())
books = [list(map(int,input().split())) for _ in range(n)]
x = list(map(int,input().split()))

ans = 10**9

for i in range(2**n):
    cost = 0
    algo = [0]*m
    for j in range(n):
        if(i>>j&1):
            cost += books[j][0]
            for k in range(m):
                algo[k] += books[j][k+1]
    if(all(a >= x for a in algo)):
        ans = min(ans,cost)

if(ans == 10**9):
    print(-1)
else:
    print(ans)
