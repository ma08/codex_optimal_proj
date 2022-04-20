


def main():
    n, k = map(int, input().split())
    t = input()
    s = t
    while len(s) < n * k:
        s += t
    print(s[:n * k])


if __name__ == '__main__':
    main()