
def main():
    n = int(input())  # number of elements in the list
    a = list(map(int, input().split()))  # list of elements
    a.sort(reverse=True)  # sort in descending order
    print(a.index(a[0]) + 1)  # print the index of the tallest person


if __name__ == '__main__':
    main()
