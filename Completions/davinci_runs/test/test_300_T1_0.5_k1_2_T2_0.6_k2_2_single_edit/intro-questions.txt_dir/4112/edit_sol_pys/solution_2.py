

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k:
        print(-1)
        return
    if k == 1:
        print(sum(A))
        return
    res = 0
    for i in range(k):
        res += A[i]
    for i in range(n - k, n):
        res += A[i]
    res_ = res
    for i in range(k, n - k):
        res_ = max(res_, res + A[i])
        res += A[i]
    print(res_)
    return

if __name__ == '__main__':
    main()
