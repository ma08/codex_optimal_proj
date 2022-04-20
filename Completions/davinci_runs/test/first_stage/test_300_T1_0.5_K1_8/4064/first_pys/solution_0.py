

n,h,l,r = map(int,input().split())
a = list(map(int,input().split()))

good = [0]*n
for i in range(n):
    good[i] = (a[i]+l)//h

ans = 0
for i in range(n):
    if good[i] == 0:
        a[i] -= 1
        good[i] = (a[i]+l)//h
    if good[i] == 1:
        ans += 1

print(ans)