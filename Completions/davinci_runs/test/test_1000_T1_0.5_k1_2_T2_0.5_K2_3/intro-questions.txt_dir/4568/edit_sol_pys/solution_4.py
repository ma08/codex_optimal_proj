

def solve(s):
    return len(set(s[:len(s) // 2]) & set(s[len(s) // 2:]))

print(solve(input()))
