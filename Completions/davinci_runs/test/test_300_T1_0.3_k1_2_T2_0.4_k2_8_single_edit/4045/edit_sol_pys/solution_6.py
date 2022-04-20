

def solve(n, s, t):
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 0
        d[s[i]] += 1
        if t[i] not in d:
            d[t[i]] = 0
        d[t[i]] += 1
    for k, v in d.items():
        if v % 2 != 0:
            return "NO"
    return "YES"


def main():
    n = int(input())
    s = input()
    t = input()
    print(solve(n, s, t))

if __name__ == "__main__":
    main()
