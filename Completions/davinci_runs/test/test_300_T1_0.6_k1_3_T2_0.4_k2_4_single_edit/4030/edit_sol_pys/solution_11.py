
n = int(input())
s = input()

def solve(n, s, cur, res):
    if n == 0:
        return res

    if n == 1 or n == 2:
        return 1 if s[0] <= s[1] else 2

    if s[0] <= s[1]:
        cur += 1
    else:
        res = max(res, cur)
        cur = 0

    return solve(n - 1, s[1:], cur, res)

print(solve(n, s))
