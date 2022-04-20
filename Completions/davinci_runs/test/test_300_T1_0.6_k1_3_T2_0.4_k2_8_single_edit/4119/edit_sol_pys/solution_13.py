


def main():
    n = int(input())
    xs = [int(x) for x in input().split()]
    # print(n, xs)

    xs.sort(reverse=True)
    print(xs[0])


if __name__ == '__main__':
    main()
