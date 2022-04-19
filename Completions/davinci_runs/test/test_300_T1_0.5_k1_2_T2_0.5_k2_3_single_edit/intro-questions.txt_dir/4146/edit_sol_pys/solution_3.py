


def main():
    n = int(input())  # n is the number of elements in the array
    a = list(map(int, input().split()))  # a is the array

    # The number of elements that need to be replaced is the number of elements
    # that are different from the first element.
    print(n - a.count(a[0]))


if __name__ == '__main__':
    main()
