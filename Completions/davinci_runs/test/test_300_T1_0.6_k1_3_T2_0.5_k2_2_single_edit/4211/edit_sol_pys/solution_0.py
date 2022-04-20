

def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    A = [0] * N
    A[0] = 0
    A[N - 1] = 0

    for i in range(1, N - 1):
        A[i] = min(B[i - 1], B[i])

    print(sum(A))

if __name__ == '__main__':
    main()
