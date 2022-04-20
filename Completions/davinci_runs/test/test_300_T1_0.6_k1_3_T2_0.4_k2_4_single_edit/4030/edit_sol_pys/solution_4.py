
n = int(input())
s = input()

def solve(n, s):
    if n == 1:
        return 1

    cur = 0
    res = 0
    for i in range(1, n):
        if s[i] < s[i - 1]:
            cur += 1
            res = max(res, cur)
        else:
            cur = 0
            
    return res + 1

print(solve(n, s))
