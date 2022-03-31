
n, k = map(int, input().split())
s = input()

ans = 0
for i in range(n):
    if s[i] == '0':
        ans += i + 1
    else:
        i += k
        if i >= n:
            break
print(ans)
