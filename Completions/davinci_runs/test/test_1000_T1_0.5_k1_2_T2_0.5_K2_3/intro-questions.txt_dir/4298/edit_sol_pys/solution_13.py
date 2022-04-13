
import sys

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    for j in range(K):
        ans += B[j] * B[j]

    print(ans)


if __name__ == "__main__":
    main()
