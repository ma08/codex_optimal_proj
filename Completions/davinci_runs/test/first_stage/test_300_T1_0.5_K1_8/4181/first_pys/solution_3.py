

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    """
    print(N, A, B)
    """

    """
    # My solution
    max_num = 0
    for i in range(N):
        if A[i] >= B[i]:
            max_num += B[i]
            A[i] -= B[i]
        else:
            max_num += A[i]
            A[i] = 0
            if A[i+1] >= B[i] - A[i]:
                max_num += B[i] - A[i]
                A[i+1] -= B[i] - A[i]
            else:
                max_num += A[i+1]
                A[i+1] = 0
    print(max_num)
    """

    # Better solution
    max_num = 0
    for i in range(N):
        if A[i] < B[i]:
            max_num += A[i]
            B[i] -= A[i]
            A[i] = 0
            if A[i+1] < B[i]:
                max_num += A[i+1]
                A[i+1] = 0
            else:
                max_num += B[i]
                A[i+1] -= B[i]
        else:
            max_num += B[i]
            A[i] -= B[i]
    print(max_num)

if __name__ == '__main__':
    main()