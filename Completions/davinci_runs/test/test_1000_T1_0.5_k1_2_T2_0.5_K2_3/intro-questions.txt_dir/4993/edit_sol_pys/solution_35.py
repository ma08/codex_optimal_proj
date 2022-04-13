import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if A[i] + A[j] == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
