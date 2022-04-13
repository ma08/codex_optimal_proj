

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    j = 0
    k = 0
    ans = 0
    for i in range(N):
        while j < N and B[j] < A[i]:
            j += 1
        while k < N and C[k] < B[j]:
            k += 1
        ans += j * k
    print(ans)


main()
