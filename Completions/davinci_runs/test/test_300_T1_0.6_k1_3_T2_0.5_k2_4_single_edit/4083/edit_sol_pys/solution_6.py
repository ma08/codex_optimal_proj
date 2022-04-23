
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_num_operations(n, k))



def min_num_operations(n, k):
    return n - k


if __name__ == '__main__':
    main()
