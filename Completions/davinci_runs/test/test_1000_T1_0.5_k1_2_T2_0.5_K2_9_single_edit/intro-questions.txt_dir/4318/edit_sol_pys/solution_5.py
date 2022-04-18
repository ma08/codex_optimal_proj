


def main():
    n = int(input())
    h = [int(input()) for i in range(n)]
    print(h.index(max(h)) + 1)


if __name__ == '__main__':
    main()
