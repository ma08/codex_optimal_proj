

def calc(n, k, A):
    if k == 1:
        return sum(A)
    if k == 2:
        return max(A)
    if k == 3:
        return max(A[0] + A[-1], max(A[1:n-1]))
    if k == 4:
        return max(A[0] + A[1] + A[-2] + A[-1], max(A[2:n-2]))
    if k == 5:
        return max(A[0] + A[1] + A[2] + A[-3] + A[-2] + A[-1], max(A[3:n-3]))
    return max(A[0] + A[1] + A[2] + A[3] + A[-4] + A[-3] + A[-2] + A[-1], max(A[4:n-4]))

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k or k == 1:
        print(calc(n, k, A))
    else:
        print(max(calc(n, k, A), calc(n, k-1, A)))
    return

if __name__ == '__main__':
    main()
