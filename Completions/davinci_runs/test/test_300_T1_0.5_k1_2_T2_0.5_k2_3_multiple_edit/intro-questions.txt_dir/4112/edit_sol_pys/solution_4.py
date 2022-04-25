

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k:
        print(-1)
        return
    ans = sum(A)
    for i in range(k):
        ans = max(ans, sum(A[:i]) + sum(A[n-k+i:]) + (k-i-1)*x)
    print(ans)
    return

if __name__ == '__main__':
    main()
