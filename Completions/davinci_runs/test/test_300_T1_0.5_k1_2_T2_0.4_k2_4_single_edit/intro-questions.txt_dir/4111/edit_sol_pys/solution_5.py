
n = int(input())
a = list(map(int, input().split()))

odd, even, ans = 0, 0, 0
for i in range(n):
    if i%2 == 0:
        odd += a[i]
    else:
        even += a[i]

ans = 0
for i in range(n):
    if i%2 == 0:
        if odd - a[i] == even:
            ans += 1
    else:
        if odd == even - a[i]:
            ans += 1

print(ans)
