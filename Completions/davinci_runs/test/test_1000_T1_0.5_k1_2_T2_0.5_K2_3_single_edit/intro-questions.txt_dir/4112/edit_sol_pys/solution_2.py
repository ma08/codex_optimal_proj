

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if k == 1:
        ans = sum(A)
    if k == 2:
        ans = max(A)
    if k == 3:
        ans = max(A[0] + A[-1], max(A[1:n-1]))
    if k == 4:
        ans = max(A[0] + A[1] + A[-2] + A[-1], max(A[2:n-2]))
    if k == 5:
        ans = max(A[0] + A[1] + A[2] + A[-3] + A[-2] + A[-1], max(A[3:n-3]))
    else:
        ans = max(A[0] + A[1] + A[2] + A[3] + A[-4] + A[-3] + A[-2] + A[-1], max(A[4:n-4]))
    if x < k:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
