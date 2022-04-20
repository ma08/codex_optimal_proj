

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k or n < k:
        print(-1)
        return
    if n == k:
        print(sum(A) + (k-1)*x)
    elif k == 1:
        print(sum(A))    
    elif k == 2:
        print(max(A))    
    elif k == 3:
        print(max(A[0] + A[-1], max(A[1:n-1])))    
    elif k == 4:
        print(max(A[0] + A[1] + A[-2] + A[-1], max(A[2:n-2])))    
    elif k == 5:
        print(max(A[0] + A[1] + A[2] + A[-3] + A[-2] + A[-1], max(A[3:n-3])))    
    else:
        print(max(A[0] + A[1] + A[2] + A[3] + A[-4] + A[-3] + A[-2] + A[-1], max(A[4:n-4])))
    return

if __name__ == '__main__':
    main()
