def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    print(A[N//2] - A[N//2-1])

if __name__ == '__main__':
    main()
