

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k - 1: return -1
    if k == 1: return sum(A)
    if k == 2: return max(A)
    if k == 3: return max(A[0] + A[-1], max(A[1:n-1]))
    if k == 4: return max(A[0] + A[1] + A[-2] + A[-1], max(A[2:n-2]))
    if k == 5: return max(A[0] + A[1] + A[2] + A[-3] + A[-2] + A[-1], max(A[3:n-3]))
    return max(A[0] + A[1] + A[2] + A[3] + A[-4] + A[-3] + A[-2] + A[-1], max(A[4:n-4]))

if __name__ == '__main__':
    print(main())
