import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))[:N]
B = list(map(int, input().split()))[:N]
C = list(map(int, input().split()))[:N - 1]


def resolve():
    ans = [0] * N
    for i in range(N):
        ans[A[i] - 1] = B[i]

    for i in range(1, N):
        ans[i] += ans[i - 1]

    for i in range(N - 1):
        ans[i] += C[i]

    print(max(ans))


if __name__ == '__main__':
    resolve()
