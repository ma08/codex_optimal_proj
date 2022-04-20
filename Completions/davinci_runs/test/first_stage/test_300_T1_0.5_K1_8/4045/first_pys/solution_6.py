

import sys

def main():
    n = int(input())
    s = input()
    t = input()

    if n == 1:
        print("YES")
        print("abc")
        return

    if s == t:
        print("NO")
        return

    print("YES")

    if s[0] == s[1]:
        print("a" * n + "b" * n + "c" * n)
    elif t[0] == t[1]:
        print("b" * n + "c" * n + "a" * n)
    else:
        print("c" * n + "a" * n + "b" * n)

if __name__ == '__main__':
    main()