
import sys


def main():
    n = int(sys.stdin.readline())
    strings = [sys.stdin.readline().strip() for i in range(n)]

    strings.sort(key=len, reverse=True)

    ok = True
    for i in range(n-1):
        if strings[i] not in strings[i+1]:
            ok = False
            break

    if ok:
        print("YES")
        for s in strings:
            print(s)
    else:
        print("NO")


if __name__ == "__main__":
    main()
