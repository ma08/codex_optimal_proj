


def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.sort()
    print(h[-1])


if __name__ == '__main__':
    main()
