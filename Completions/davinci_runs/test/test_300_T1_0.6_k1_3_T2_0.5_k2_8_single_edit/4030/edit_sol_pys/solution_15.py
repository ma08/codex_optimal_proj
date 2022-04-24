
n = int(input())
s = input()

def solve(n, s, start):
    if n == 1:
        return 1
    if n == 2:
        return 1 if s[0] <= s[1] else 2

    cur = 0
    res = 0
    for i in range(start + 1, n):
        if s[i] < s[i - 1]:
            cur += 1
            res = max(res, cur)
        else:
            cur = 0
            
    return res + 1

print(solve(n, s))
