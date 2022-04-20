
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    while K > 0:
        K -= 1
        if N % 2 == 0:
            A = A[N//2:] + A[:N//2]
        else:
            A = A[N//2+1:] + A[:N//2+1]
    print(*A)

if __name__ == '__main__':
    main()
