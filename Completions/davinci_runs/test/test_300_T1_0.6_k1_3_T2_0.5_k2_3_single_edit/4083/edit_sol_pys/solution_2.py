
def main():
    n, k = map(int, input().split())  # n: the number of elements, k: the number of operations
    a = list(map(int, input().split()))  # a: the list of elements
    print(min_num_operations(n, k, a))  # the minimum number of operations


def min_num_operations(n, k, a):
    return n - k


if __name__ == '__main__':
    main()
