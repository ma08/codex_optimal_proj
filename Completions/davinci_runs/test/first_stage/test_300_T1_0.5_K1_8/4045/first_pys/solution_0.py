

import sys

def find_string(n, s, t):
    if n == 1:
        if s[0] != t[0] and s[1] != t[1]:
            return "YES\n" + s[0] + s[1] + t[0] + t[1] + s[0] + s[1]
        return "NO"
    if s[0] == s[1]:
        return "NO"
    if t[0] == t[1]:
        return "NO"
    if s[0] == t[0] or s[0] == t[1] or s[1] == t[0] or s[1] == t[1]:
        return "NO"
    return "YES\n" + s[0] * n + s[1] * n + t[0] * n + t[1] * n + s[0] * n + s[1] * n

def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    print(find_string(n, s, t))

if __name__ == "__main__":
    main()