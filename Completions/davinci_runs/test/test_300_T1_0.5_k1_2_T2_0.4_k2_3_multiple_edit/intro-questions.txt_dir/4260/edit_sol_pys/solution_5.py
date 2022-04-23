def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(A)
    ans = 0
    for i in range(M):
        if A[i] >= 0:
            break
        ans -= A[i]
    print(ans)

if __name__ == '__main__':
    main()
