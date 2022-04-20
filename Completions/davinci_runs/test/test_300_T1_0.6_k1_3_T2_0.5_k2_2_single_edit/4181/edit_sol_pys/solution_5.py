

import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # The first hero can defeat at most B[0] monsters attacking the first town, so he will defeat B[0] monsters attacking the first town.
    # The second hero can defeat at most B[0] + B[1] monsters attacking the first and second town, so he will defeat B[1] monsters attacking the second town.
    # The i-th hero can defeat at most B[0] + B[1] + ... + B[i-1] + B[i] monsters attacking the first, second, ..., (i-1)-th, and i-th towns, so he will defeat B[i-1] monsters attacking the (i-1)-th town.
    # The last hero can defeat at most B[0] + B[1] + ... + B[N-1] + B[N] monsters attacking the first, second, ..., (N-1)-th, and N-th towns, so he will defeat B[N-1] monsters attacking the (N-1)-th town.
    # The total number of monsters defeated is B[0] + B[1] + ... + B[N-1].
    # However, some monsters may have already been defeated.
    # For example, if B[0] + B[1] < A[0] + A[1], the third hero must defeat at least A[0] + A[1] - (B[0] + B[1]) monsters attacking the third town.
    # In such case, the total number of monsters defeated is B[0] + B[1] + ... + B[N-1] + (A[0] + A[1] - (B[0] + B[1])) + (A[1] + A[2] - (B[1] + B[2])) + ... + (A[N] + A[N+1] - (B[N-1] + B[N])).
    # This can be simplified as B[0] + B[1] + ... + B[N-1] + A[0] + A[1] + ... + A[N+1] - (B[0] + B[1] + ... + B[N-1] + B[0] + B[1] + ... + B[N-1] + B[1] + B[2] + ... + B[N-1] + ... + B[N-2] + B[N-1] + B[N])
    # This can be simplified as B[0] + B[1] + ... + B[N-1] + A[0] + A[1] + ... + A[N+1] - (N * B[0] + (N-1) * B[1] + ... + 2 * B[N-1] + B[N])

    total = 0
    for i in range(N):
        total += B[i]
    for i in range(N + 1):
        total += A[i]
    for i in range(N):
        total -= (N-i) * B[i]
    print(total)

if __name__ == "__main__":
    main()
