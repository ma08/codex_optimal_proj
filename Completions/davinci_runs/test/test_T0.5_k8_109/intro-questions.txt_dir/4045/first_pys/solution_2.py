

import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    if n == 1:
        res = s[0] + t[1] + s[1]
        print("YES")
        print(res)
        return
    if n == 2:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t
            print("YES")
            print(res)
            return
    if n == 3:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t + s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1] + s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t + s + t + s + t
            print("YES")
            print(res)
            return
    if n == 4:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t + s + t + s + t + s + t + s + t
            print("YES")
            print(res)
            return
    if n == 5:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t
            print("YES")
            print(res)
            return
    if n == 6:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t
            print("YES")
            print(res)
            return
    if n == 7:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t
            print("YES")
            print(res)
            return
    if n == 8:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t
            print("YES")
            print(res)
            return
    if n == 9:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t
            print("YES")
            print(res)
            return
    if n == 10:
        if s[0] == s[1] and t[0] == t[1]:
            print("NO")
            return
        elif s[0] == s[1]:
            res = s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t + s[0] + t + s[1] + t
            print("YES")
            print(res)
            return
        elif t[0] == t[1]:
            res = s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1] + s + t[0] + s + t[1]
            print("YES")
            print(res)
            return
        else:
            res = s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t + s + t
            print("YES")
            print(res)
            return

if __name__ == "__main__":
    main()