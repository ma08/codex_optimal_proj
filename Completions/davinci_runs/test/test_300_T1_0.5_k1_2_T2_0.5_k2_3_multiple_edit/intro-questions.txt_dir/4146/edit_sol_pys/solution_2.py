
def main():
    n = int(input())
    a = list(map(int, input().split()))  # a = [int(input()) for i in range(n)]

    # The number of elements that need to be replaced is the number of elements
    # that are different from the first element.
    print(n - a.count(a[0]))


if __name__ == '__main__':
    main()
