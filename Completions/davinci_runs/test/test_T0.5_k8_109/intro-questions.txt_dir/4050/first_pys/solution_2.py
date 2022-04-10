

# Solution

n = int(input())
a = list(map(int, input().split()))

s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]

d = {}
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        d[s[j] - s[i]] = d.get(s[j] - s[i], []) + [(i, j)]

ans = []
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        if s[j] - s[i] in d:
            for x in d[s[j] - s[i]]:
                if x[1] <= i or x[0] >= j:
                    ans.append((i, j))
ans = sorted(list(set(ans)))
print(len(ans))
for x in ans:
    print(*x)