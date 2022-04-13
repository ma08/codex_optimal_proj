
def main():
    k = int(input())

    # The number of elements that need to be replaced is the number of elements that are different from the first element.
    print(k - a.count(a[0]))


if __name__ == '__main__':
    main()
