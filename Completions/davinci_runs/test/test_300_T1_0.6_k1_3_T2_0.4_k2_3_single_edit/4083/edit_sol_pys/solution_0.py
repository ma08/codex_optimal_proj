
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(min_num_operations(N, K, A))



def min_num_operations(N, K, A):
    return N - K


if __name__ == '__main__':
    main()
