
import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    if s[0] == s[1] or t[0] == t[1]:
        print("NO")
        return

    if s[0] == t[0] or s[0] == t[1] or s[1] == t[0] or s[1] == t[1]:
        print("NO")
        return

    res = ""
    for i in range(n):
        res += s[0]
        res += t[0]
        res += s[1]
    print("YES")
    print(res)

if __name__ == "__main__":
    main()
