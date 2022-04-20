

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k:
        print(-1)
        return
    ans = 0
    for i in range(k):
        ans += A[i]
    for i in range(n-k, n):
        ans += A[i]
    print(ans)
    return

if __name__ == '__main__':
    main()
