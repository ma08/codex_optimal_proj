
a = []

def main():
    n = int(input("enter the number of elements"))
    for i in range(n):
        a.append(int(input("enter the elements")))
    print(a)

    # The number of elements that need to be replaced is the number of elements
    # that are different from the first element.
    print(n - a.count(a[0]))


if __name__ == '__main__':
    main()
