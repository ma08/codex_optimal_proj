

n,k,m = map(int,input().split())
a = list(map(int,input().split()))

total = sum(a)
ave = total / n

ans = m * n - total

if ans < 0:
    print(-1)
else:
    if ans > k:
        print(-1)
    else:
        print(int(ans))