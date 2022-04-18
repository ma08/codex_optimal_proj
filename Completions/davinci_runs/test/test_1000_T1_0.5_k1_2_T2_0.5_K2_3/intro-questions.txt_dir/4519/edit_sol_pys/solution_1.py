def solve(n, k, s):
    s = list(s)
    while k > 0:
        for i in range(n - 1):
            if s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
                k -= 1
                changed = True
                break
        if not changed:
            break
    return "".join(s)


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
