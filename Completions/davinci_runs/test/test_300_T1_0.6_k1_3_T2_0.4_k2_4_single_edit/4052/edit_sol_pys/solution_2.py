
n = int(input())
s = input()
t = input()

def swap(s, i, j):
    return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

def diff(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return i
    return len(s)

def solve(s, t):
    if s == t:
        return 0

    i = diff(s, t)
    if i == len(s):
        return -1

    j = i + 1
    while j < len(s) and s[j] == t[i]:
        j += 1
    if j < len(s) and s[j] == t[j]:
        s = swap(s, i, j)
        return 1 + solve(s, t)

    j = i + 1
    while j < len(s) and s[j] != t[j]:
        j += 1
    if j < len(s):
        s = swap(s, i, j)
        return 1 + solve(s, t)
    else:
        return -1

def solve_slow(s, t):
    # print(s, t)
    if s == t:
        return 0

        return 0

    for i in range(len(s) - 1):
        if s[i] != t[i] and s[i + 1] != t[i + 1]:
            s = swap(s, i, i + 1)
            return 1 + solve(s, t)
    return -1

result = solve(s, t)
if result == -1:
    print(-1)
else:
    print(result)
    i = diff(s, t)
    j = i + 1
    while j < len(s) and s[j] == t[i]:
        j += 1
    if j < n and s[j] == t[j]:
        print(i + 1, j + 1)
    else:
        print(i + 1, j + 1)
        i = diff(s, t)
        j = i + 1
        while j < len(s) and s[j] != t[j]:
            j += 1
        print(i + 1, j + 1)
