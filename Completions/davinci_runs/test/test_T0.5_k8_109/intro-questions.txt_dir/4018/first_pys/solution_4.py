


def main():
    n, k = map(int, input().split())
    s = input()
    if k > n ** 2:
        print(-1)
    else:
        print(n * (n + 1) // 2 - n + k)


if __name__ == "__main__":
    main()