

def solve(s):
    return len(set(s[:len(s)//2]) & set(s[len(s)//2:])) if len(s)%2 == 0 else -1

print(solve(input()))
