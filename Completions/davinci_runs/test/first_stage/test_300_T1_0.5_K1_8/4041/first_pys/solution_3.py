

def solve(s, t):
    i = 0
    j = 0
    count = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        else:
            count += 1
        i += 1
    return count + len(s) - i

s = input()
t = input()
print(solve(s, t))