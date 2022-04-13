
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split())) # a is list

    # The number of elements that need to be replaced is the number of
    # elements that are different from the first element.
    print(n - a.count(a[0]))
