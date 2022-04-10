

s = input()
t = input()


def solve(s, t):
    l = 0
    r = 0
    n = len(t)
    ans = 0
    while l < n:
        if r >= len(s):
            return 0
        if s[r] == t[l]:
            l += 1
        r += 1
    r -= 1
    while r < len(s):
        while l < n and s[r] != t[l]:
            r += 1
        if r >= len(s):
            return 0
        ans = max(ans, r - l)
        l += 1
        r += 1
    return ans


print(solve(s, t))