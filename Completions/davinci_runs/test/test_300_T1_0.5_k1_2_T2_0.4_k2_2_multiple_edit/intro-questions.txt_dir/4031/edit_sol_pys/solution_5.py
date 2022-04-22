import sys


def main():
    n = int(sys.stdin.readline())
    strings = []
    for _ in range(n):
        strings.append(sys.stdin.readline().strip())

    strings.sort(key=len, reverse=True)

    ok = True
    for i in range(1, n):
        for j in range(i):  # noqa: E203
            if strings[i] not in strings[j]:  # noqa: E203
                ok = False
                break
        if not ok:
            break

    if ok:
        print("YES")
        print("\n".join(strings))
    else:
        print("NO")


if __name__ == "__main__":
    main()
