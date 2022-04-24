

def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    A = [0] * N
    for i in range(N):
        if i == 0:
            A[i] = B[i]
        elif i == N - 1:
            A[i] = B[i - 1]
        else:
            A[i] = min(B[i - 1], B[i])
    print(sum(A))

if __name__ == '__main__':
    main()
