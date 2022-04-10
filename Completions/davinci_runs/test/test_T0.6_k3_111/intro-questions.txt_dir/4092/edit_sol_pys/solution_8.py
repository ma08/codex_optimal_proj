n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] < 0:
        ans += 1
        a[i] = -a[i]
ans += sum(a)
if ans % 2 == 0:
    print(ans)
else:
    print(ans - min(a) * 2)
