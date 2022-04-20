

n = int(input())
a = list(map(int, input().split()))

s = []
for i in range(n):
    s.append(sum(a[i:]))

m = []
for i in range(n):
    m.append(s[i])
    for j in range(i):
        if s[j] == s[i]:
            m[i] = min(m[i], m[j] + 1)

print(min(m))
for i in range(n):
    if m[i] == min(m):
        print(i+1, i+1)