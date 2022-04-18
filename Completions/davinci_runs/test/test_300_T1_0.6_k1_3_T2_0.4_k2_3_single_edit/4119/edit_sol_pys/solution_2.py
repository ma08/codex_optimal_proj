

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i > 0 and A[i-1] + 1 == A[i]:
            ans += C[A[i-1]-1]
    print(ans)

if __name__ == '__main__':
    main()
