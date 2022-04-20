
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    prev = -1
    ans = 0
    for i in range(N):
        if prev + 1 == A[i]:
            ans += C[prev]
        ans += B[A[i]-1]
        prev = A[i]
    print(ans)


if __name__ == '__main__':
    main()
