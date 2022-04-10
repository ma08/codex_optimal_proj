

def solve(n, s, t):
    if s[0] == s[1] or t[0] == t[1] or s[0] == t[0] or s[1] == t[1]:
        return 'NO'
    for c in ['a', 'b', 'c']:
        if c not in [s[0], s[1], t[0], t[1]]:
            return (s[0] * n + c * n + t[0] * n)
    return 'NO'

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    t = input().strip()
    print(solve(n, s, t))
