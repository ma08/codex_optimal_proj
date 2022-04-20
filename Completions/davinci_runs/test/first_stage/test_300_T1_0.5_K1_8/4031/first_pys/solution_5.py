


def main():
    n = int(input())
    strings = [input() for _ in range(n)]
    strings.sort(key=lambda s: len(s), reverse=True)
    for i in range(1, n):
        if not strings[i].startswith(strings[i - 1]):
            return print("NO")
    print("YES")
    print("\n".join(strings))


if __name__ == "__main__":
    main()