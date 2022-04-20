

def solve(n, s, t):
    res = ""
    if s[0] == s[1] and t[0] == t[1]:
        if s[0] == t[0]:
            return "NO"
        for i in range(n):
            res += s[0]
            res += t[0]
            res += s[1]
    elif s[0] == s[1]:
        if s[0] == t[0] or s[0] == t[1]:
            return "NO"
        for i in range(n):
            res += s[0]
            res += t[0]
            res += s[1]
    elif t[0] == t[1]:
        if t[0] == s[0] or t[0] == s[1]:
            return "NO"
        for i in range(n):
            res += s[0]
            res += t[0]
            res += s[1]
    else:
        for i in range(n):
            res += s[0]
            res += t[0]
            res += s[1]
    return res

def main():
    n = int(input())
    s = input()
    t = input()
    print(solve(n, s, t))

if __name__ == "__main__":
    main()
