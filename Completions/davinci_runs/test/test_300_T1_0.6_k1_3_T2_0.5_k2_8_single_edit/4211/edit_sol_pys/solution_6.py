
def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N - 1):
        B[i] = min(A[i - 1], A[i])
    B[N - 1] = A[N - 2]
    print(sum(B))

if __name__ == '__main__':
    main()
