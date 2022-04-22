
def solve(n, k, a):
    ans = 0
    for i in range(n):
        if a[i] % 2 == 1:
            a[i] -= 1
            ans += 1

ans = 0
for i in range(n):
    if a[i] % 2 == 1:
        a[i] -= 1
        ans += 1

if sum(a) // k < 2:
    print(ans)
else:
    print(ans + sum(a) // k - 1)
