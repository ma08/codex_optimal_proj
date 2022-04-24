# https://codeforces.com/problemset/problem/127/B

import sys


def main():
    n = int(sys.stdin.readline())
    strings = []
    for i in range(n):
        strings.append(sys.stdin.readline().strip())

    strings.sort(key=len, reverse=True)

    ok = "YES"
    for i in range(n):
        for j in range(i):
            if strings[i] not in strings[j]:
                ok = "NO"
                break

    print(ok)
    for s in strings:
        print(s)


if __name__ == "__main__":
    main()
