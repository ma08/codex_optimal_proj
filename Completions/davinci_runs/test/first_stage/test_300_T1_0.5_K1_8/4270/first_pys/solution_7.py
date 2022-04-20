


def main():
    """
    Main function
    """
    import sys
    input = sys.stdin.readline

    n = int(input())
    values = list(map(int, input().split()))

    values.sort()
    for i in range(n - 1):
        values[i + 1] = (values[i] + values[i + 1]) / 2

    print(values[-1])


if __name__ == '__main__':
    main()