
n, k = map(int, input().split())
t = input()

ans = ""
for i in range(n):
    if i < (k - 1) % n + 1:
        ans += t[i]
    else:
        ans += t[(k - 1) % n + 1]

print(ans)
