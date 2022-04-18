

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0

for i in range(3):
    if a[i] == n or b[i] == n:
        continue
    else:
        if (i - i) % 3 == 1:
            ans += min(a[i],b[i])
        elif (i - i) % 3 == 2:
            ans += min(a[i],b[i])

print(ans,n-ans)
