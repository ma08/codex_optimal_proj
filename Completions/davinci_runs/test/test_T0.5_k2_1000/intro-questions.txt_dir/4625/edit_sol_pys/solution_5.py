t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    p.append(n)
    d = {}
    c = 0
    for i in range(n):
        if i == p[c]:
            c += 1
        d[s[i]] = d.get(s[i], 0) + (n - p[c])
    for i in d:
        print(d[i], end=" ")
    print()
