
import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    if s[0] == s[1] or t[0] == t[1] or s[0] == t[0] or s[0] == t[1] or s[1] == t[0] or s[1] == t[1]:
        print("NO")
        return

    print("YES")
    for i in range(n): print(s[0]+t[0]+s[1], end="")

if __name__ == "__main__":
    main()
