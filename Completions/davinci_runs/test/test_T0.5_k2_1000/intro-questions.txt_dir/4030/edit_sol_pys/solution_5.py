
n = int(input())
s = input()

if n == 1:
    print(1, 1)
    print(1)
    exit()

if n == 2:
    if s[0] < s[1]:
        print(2)
        print(2, 1)
    else:
        print(1)
        print(1, 1)
    exit()

c = [1] * n

if s[0] < s[1]:
    c[0] = 2

if s[n - 1] > s[n - 2]:
    c[n - 1] = 2

for i in range(1, n - 1):
    if s[i] < s[i + 1]:
        c[i] = max(c[i], c[i + 1])
        c[i + 1] = max(c[i], c[i + 1])
    if s[i] > s[i - 1]:
        c[i] = max(c[i], c[i - 1])
        c[i - 1] = max(c[i], c[i - 1])

print(max(c))
print(*c)
