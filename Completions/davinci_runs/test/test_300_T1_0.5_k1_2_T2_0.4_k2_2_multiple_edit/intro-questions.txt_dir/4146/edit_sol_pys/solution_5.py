
# b

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split())) + [0]

    # The number of elements that need to be replaced is the sum of the
    # differences between the numbers of adjacent elements.
    print(sum(max(a[i + 1] - a[i] - m, 0) for i in range(n)))


if __name__ == '__main__':
    main()
