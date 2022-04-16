

def solve(s):
    return len(set(s[:len(s)//2]) & set(s[(len(s)//2)+1:]))

print(solve(input()))
