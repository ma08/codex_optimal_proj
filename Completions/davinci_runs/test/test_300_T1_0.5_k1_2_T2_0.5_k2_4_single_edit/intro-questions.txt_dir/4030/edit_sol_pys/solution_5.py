
n = int(input())
s = input()

c = [1] * n

if n > 1 and s[0] > s[1]:
    c[0] = 2

if n > 1 and s[n - 1] < s[n - 2]:
    c[n - 1] = 2

for i in range(1, n - 1):
    if s[i] > s[i + 1] and c[i] <= c[i + 1]:
        c[i] = max(c[i], c[i + 1])
        c[i + 1] = max(c[i], c[i + 1])
    if s[i] < s[i - 1] and c[i] <= c[i - 1]:
        c[i] = max(c[i], c[i - 1])
        c[i - 1] = max(c[i], c[i - 1])

print(max(c))
print(*c)
