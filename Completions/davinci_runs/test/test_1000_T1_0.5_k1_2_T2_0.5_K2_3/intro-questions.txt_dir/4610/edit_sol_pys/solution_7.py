

def main():
    N = int(input())
    A = list(map(int, input().split()))[::-1]
    B = [0] * N
    for i in range(N):
        if A[i] != N - i:
            B[A[i]] = 1
    print(B.index(0))


if __name__ == '__main__':
    main()
