
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    p.append(n)
    ans = dict()
    c = 0
    for i in range(n):
        if i == p[c]:
            c += 1
        ans[s[i]] = ans.get(s[i], 0) + n - p[c]
    for i in ans:
        print(ans[i], end=" ")
    print()
