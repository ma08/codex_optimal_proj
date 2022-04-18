


def main():
    n, k = map(int, input().split())
    l = sorted(list(map(int, input().split())), reverse=True)
    print(sum(l[:k]))


if __name__ == '__main__':
    main()
