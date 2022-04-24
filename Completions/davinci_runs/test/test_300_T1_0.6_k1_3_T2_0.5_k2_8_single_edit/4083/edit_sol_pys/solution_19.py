
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_num_operations(n, k, a))


def min_num_operations(n, k, a):
    return n - k



if __name__ == '__main__':
    main()
