import math



def main():
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    A.sort()
    # print(A)
    ans = float('inf')
    for i in range(N - K + 1):
        ans = min(ans, A[i + K - 1] - A[i])
    print(ans)


main()
