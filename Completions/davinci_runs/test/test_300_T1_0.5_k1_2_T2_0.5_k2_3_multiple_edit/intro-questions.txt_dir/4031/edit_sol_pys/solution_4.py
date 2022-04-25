
# https://codeforces.com/contest/1186/problem/C
import sys


def main():
    n = int(sys.stdin.readline())
    strings = [''] * n
    for i in range(n):
        strings[i] = sys.stdin.readline().strip()

    strings.sort(key=len)

    ok = True
    for i in range(n):
        for j in range(i+1, n):
            if strings[j] not in strings[i]:
                ok = False
                break
        if not ok:
            break

    if ok:
        print("YES")
        for s in strings:
            print(s)
    else:
        print("NO")


if __name__ == "__main__":
    main()
