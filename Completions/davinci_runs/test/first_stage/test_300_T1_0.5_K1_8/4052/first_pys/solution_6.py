

n = int(input())
s = list(input())
t = list(input())

def check(s, t):
    for i in range(n):
        if s[i] != t[i]:
            return False
    return True

def swap(s, i, j):
    s[i], s[j] = s[j], s[i]
    return s

def solve(s, t):
    if check(s, t):
        return 0
    if len(s) == 1:
        return -1
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == t[j] and s[j] == t[i]:
                return solve(swap(s, i, j), t) + 1
    return -1

print(solve(s, t))