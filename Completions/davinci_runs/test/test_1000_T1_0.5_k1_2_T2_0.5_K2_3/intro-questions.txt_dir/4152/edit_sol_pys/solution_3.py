
def solve(A, N):
    memo = [False] * (2 ** 20)
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] + A[j] < 2 ** 20:
                memo[A[i] + A[j]] = True
    return N - sum(memo)


def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    print(solve(A, n))


if __name__ == "__main__":
    main()
