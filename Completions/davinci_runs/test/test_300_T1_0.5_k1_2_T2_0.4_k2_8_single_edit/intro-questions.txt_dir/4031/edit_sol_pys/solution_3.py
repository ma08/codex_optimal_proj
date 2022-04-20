import sys


def main():
    n = int(sys.stdin.readline())
    strings = []
    for i in range(n):
        strings.append(sys.stdin.readline().strip())

    strings.sort(key=len, reverse=True)

    ok = True
    for i in range(n):
        for j in range(i):
            if strings[i] not in strings[j]:  # noqa: E712
                ok = False
                break
        if not ok:
            break

    if ok:
        print("YES")  # noqa: E712
        for s in strings:
            print(s)
    else:
        print("NO")  # noqa: E712


if __name__ == "__main__":
    main()
