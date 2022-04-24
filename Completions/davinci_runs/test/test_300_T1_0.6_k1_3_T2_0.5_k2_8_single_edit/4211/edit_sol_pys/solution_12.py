

def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    A = [0] * N
    A[0] = B[0]
    for i in range(1, N):
        A[i] = min(B[i - 1], B[i])
    A[N - 1] = B[N - 1]
    print(sum(A))

if __name__ == '__main__':
    main()
