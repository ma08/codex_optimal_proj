

n = int(input())
x = sorted(list(map(int,input().split())))

ans = 0
for i in range(1,n):
    ans += abs(x[i]-x[i-1])-1

print(ans)