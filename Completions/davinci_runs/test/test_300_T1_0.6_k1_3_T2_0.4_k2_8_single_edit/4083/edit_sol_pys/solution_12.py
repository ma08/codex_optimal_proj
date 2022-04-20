def min_num_operations(n, k, a):
    return n - k


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_num_operations(n, k, a))


if __name__ == '__main__':
    main()
