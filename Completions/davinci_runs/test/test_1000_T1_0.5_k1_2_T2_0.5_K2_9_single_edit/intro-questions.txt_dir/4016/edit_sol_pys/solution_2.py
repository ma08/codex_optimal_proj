
n, k = map(int, input().split())
s = input()

ans = ""
for i in range(n):
    if i < (k - 1) % n:
        ans += s[i]
    else:
        ans += s[(k - 1) % n]

print(ans)
