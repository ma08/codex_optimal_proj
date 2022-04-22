
n, m = map(int, input().split())
a = list(map(int, input().split()))

c = {}
for i in range(n):
    if c.get(a[i]):
        c[a[i]] += 1
    else:
        c[a[i]] = 1

if s == s[::-1]:
    print(0)
    exit()

for i in range(len(s) // 2):
    if s[i] == s[-1 - i]:
        continue
    else:
        print(1)
        break
else:
    print(1)
