# https://atcoder.jp/contests/abc085/tasks/abc085_c


def main():
    n = int(input())
    n, y = map(int, input().split())

    # The number of elements that need to be replaced is the number of elements
    # that are different from the first element.
    print(n - a.count(a[0]))


if __name__ == '__main__':
    main()
