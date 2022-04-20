

import sys

def main() -> None:
    n = int(input())
    s = input()
    t = input()

    if s == t:
        print("NO")
        return

    s0 = s[0]
    s1 = s[1]
    t0 = t[0]
    t1 = t[1]

    if s0 != t0 and s0 != t1 and s1 != t0 and s1 != t1:
        print("YES")
        print(s0*n + s1*n + t0*n + t1*n)
        return

    if s0 != s1 and t0 != t1:
        print("YES")
        print(s0*n + t0*n + s1*n + t1*n)
        return

    if s0 != t0:
        print("YES")
        print(s0*n + t0*n + s1*n + t1*n + s0*n)
        return

    if s0 != t1:
        print("YES")
        print(s0*n + t1*n + s1*n + t0*n + s0*n)
        return

    print("NO")
    return

if __name__ == '__main__':
    main()