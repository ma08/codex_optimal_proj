
n = int(input())

ans = 0
for a in range(1, n):
    b = n / a
    if b.is_integer():
        ans += 1

print(ans)
