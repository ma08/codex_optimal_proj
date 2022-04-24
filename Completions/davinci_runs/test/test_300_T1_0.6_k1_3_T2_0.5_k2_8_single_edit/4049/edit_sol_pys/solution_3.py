

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0

for i in range(n):
    if a[i] == b[i]:
        continue    
    elif (a[i] - b[i])%3 == 1:
        ans += min(a[i],b[i])
    elif (a[i] - b[i])%3 == 2:
        ans += min(a[i],b[i])

print(ans,n-ans)
