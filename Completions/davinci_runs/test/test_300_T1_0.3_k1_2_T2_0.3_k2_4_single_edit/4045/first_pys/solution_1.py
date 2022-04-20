

def solve(n, s, t):
    if s[0] == s[1] or t[0] == t[1]:
        return "NO"
    if s[0] == t[0] or s[0] == t[1] or s[1] == t[0] or s[1] == t[1]:
        return "NO"
    res = ""
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