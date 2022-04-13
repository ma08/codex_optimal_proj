def main():
    n = int(input())
    a = list(map(int, input().split()))

    # # The number of elements that need to be replaced is the number of
    # # elements that are different from the first element.
    # print(n - a.count(a[0]))


    # # The number of elements that need to be replaced is the number of
    # # elements that are different from the last element.
    # print(n - a.count(a[-1]))

    # The number of elements that need to be replaced is the number of
    # elements that are different from the smallest element.
    print(n - a.count(min(a)))
