

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    for i in range(1, N - 1):
        A[i] = min(B[i - 1], B[i])
    A[N - 1] = B[N - 2]
    print(sum(A))

if __name__ == '__main__':
    main()
