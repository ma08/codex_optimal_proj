
s = input()
l = len(s)
ans = 0
for i in range(l):
    if s[i] == 'U':
        ans += l - i - 1 + 2 * i
    else:
        ans += 2 * (l - i - 1) + i
print(ans)
