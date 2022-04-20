

import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    if s == t:
        print(0)
        return
    if n == 2 and s[0] == t[1] and s[1] == t[0]:
        print(1)
        print(1)
        return
    if n == 2:
        print(-1)
        return
    for i in range(n - 1):
        if s[i] == t[i] and s[i + 1] == t[i + 1]:
            continue
        elif s[i] == t[i + 1] and s[i + 1] == t[i]:
            print(1)
            print(i + 1)
            return
        elif s[i] == t[i] and s[i + 1] == t[i + 2] and s[i + 2] == t[i + 1]:
            print(2)
            print(i + 2, i + 2)
            return
        elif s[i] == t[i + 2] and s[i + 1] == t[i + 1] and s[i + 2] == t[i]:
            print(2)
            print(i + 2, i + 1)
            return
        elif s[i] == t[i + 1] and s[i + 1] == t[i + 2] and s[i + 2] == t[i]:
            print(3)
            print(i + 1, i + 2, i + 2)
            return
        elif s[i] == t[i + 2] and s[i + 1] == t[i] and s[i + 2] == t[i + 1]:
            print(3)
            print(i + 1, i + 1, i + 2)
            return
    print(-1)

if __name__ == '__main__':
    main()