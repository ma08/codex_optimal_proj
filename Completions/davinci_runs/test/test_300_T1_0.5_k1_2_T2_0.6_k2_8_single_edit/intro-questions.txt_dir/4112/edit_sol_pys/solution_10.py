

def main():
    if n < k:
        print(-1)
        return
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k:
        print(-1)
        return
    if n == k:
        print(sum(A))
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, sum(A[i:i+k]))
    print(ans)
    return

if __name__ == '__main__':
    main()
