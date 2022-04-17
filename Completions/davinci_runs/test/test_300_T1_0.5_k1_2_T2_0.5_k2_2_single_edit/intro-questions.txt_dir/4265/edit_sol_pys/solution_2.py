def solve(s, t):
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    return ans


s = input()
t = input()

print(solve(s, t))
