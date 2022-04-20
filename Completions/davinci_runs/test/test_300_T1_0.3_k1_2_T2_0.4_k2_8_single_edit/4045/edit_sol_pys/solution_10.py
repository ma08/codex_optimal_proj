
import sys

def main():
    n = int(input())
    s = input().strip()
    t = input().strip()

    if s[0] == s[1] or t[0] == t[1]:
        print("no")
        return

    if s[0] == t[0] or s[0] == t[1] or s[1] == t[0] or s[1] == t[1]:
        print("no")
        return

    res = ""
    for i in range(n):
        res += s[0]
        res += t[0]
        res += s[1]
    print("yes")
    print(res)

if __name__ == "__main__":
    main()
