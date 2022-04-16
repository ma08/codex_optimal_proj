

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k:
        print(-1)
        return
    elif k == 1:
        print(sum(A))
        return
    elif k == 2:
        print(max(A))
        return
    elif k == 3:
        print(max(A[0] + A[-1], max(A[1:n-1])))
        return
    elif k == 4:
        print(max(A[0] + A[1] + A[-2] + A[-1], max(A[2:n-2])))
        return
    elif k == 5:
        print(max(A[0] + A[1] + A[2] + A[-3] + A[-2] + A[-1], max(A[3:n-3])))
        return
    else:
        print(max(A[0] + A[1] + A[2] + A[3] + A[-4] + A[-3] + A[-2] + A[-1], max(A[4:n-4])))
        return

if __name__ == '__main__':
    main()
