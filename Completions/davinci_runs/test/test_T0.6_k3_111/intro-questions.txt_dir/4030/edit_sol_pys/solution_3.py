
n = int(input())
s = input()


def solve(n, s,):
    c = [1] * n
    for i in range(n - 1):
        if s[i] < s[i + 1]:
            continue
        c[i] = 2
        for j in range(i + 1, n):
            if s[j] > s[i]:
                c[j] = 2
    if c == [1] * n:
        return 1, c
    for i in range(n - 1):
        if c[i] != c[i + 1]:
            continue
        c[i + 1] = 3
        for j in range(i + 1, n):
            if c[j] == c[i]:
                c[j] = 3
        break
    return max(c), c

ans, c = solve(n, s)
print(ans)
print(*c)
