


def main():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    print(len(list(filter(lambda x: x < a[n - 1], a))))


if __name__ == '__main__':
    main()
