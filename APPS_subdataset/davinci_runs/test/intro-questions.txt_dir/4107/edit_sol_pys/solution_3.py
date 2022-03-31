n, k = map(int, input().split())
s = input()

ans = 0
for i in range(n):
    if s[i] == '0':
        ans += i + 1
    else:
        if i + k <= n:
            ans += i + k
        else:
            i = n
print(ans)
