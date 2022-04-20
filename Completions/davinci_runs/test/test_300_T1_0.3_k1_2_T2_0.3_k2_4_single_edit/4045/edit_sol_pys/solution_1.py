

def solve(n, s, t):
    res = ""
    for i in range(n):
        res += s[0]
        res += t[0]
        res += s[1]
    return "YES\n" + res

def main():
    n = int(input())
    s = input()
    t = input()
    print(solve(n, s, t))

if __name__ == "__main__":
    main()
