
import sys


def main():
    n = int(sys.stdin.readline())
    strings = []
    for i in range(n):
        strings.append(sys.stdin.readline().strip())

    strings.sort(key=len, reverse=True)

    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
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
