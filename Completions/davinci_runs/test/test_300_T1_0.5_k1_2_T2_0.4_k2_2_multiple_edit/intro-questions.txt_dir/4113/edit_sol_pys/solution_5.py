

N = int(input())
A = list(map(int, input().split()))


def solve(N, A):
    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] //= 2
            count += 1
    return count


print(solve(N, A))
