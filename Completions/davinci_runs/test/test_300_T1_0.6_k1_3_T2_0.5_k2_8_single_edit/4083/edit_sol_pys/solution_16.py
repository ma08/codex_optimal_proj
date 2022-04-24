
def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    print(min_num_operations(n, a))


def min_num_operations(n, a):
    return n


if __name__ == '__main__':
    main()
