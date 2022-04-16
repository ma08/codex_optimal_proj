


def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    print(sum(l[:k]))


if __name__ == '__main__':
    main()