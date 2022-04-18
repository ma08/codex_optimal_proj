

import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # The first hero can defeat at most B_1 monsters attacking the first town, so he will defeat B_1 monsters attacking the first town.
    # The second hero can defeat at most B_1 + B_2 monsters attacking the first and second town, so he will defeat B_2 monsters attacking the second town.
    # The i-th hero can defeat at most B_1 + B_2 + ... + B_{i-1} + B_i monsters attacking the first, second, ..., (i-1)-th, and i-th towns, so he will defeat B_{i} monsters attacking the i-th town.
    # The last hero can defeat at most B_1 + B_2 + ... + B_{N-1} + B_N monsters attacking the first, second, ..., (N-1)-th, and N-th towns, so he will defeat B_{N} monsters attacking the N-th town.
    # The total number of monsters defeated is B_1 + B_2 + ... + B_{N-1}.
    # However, some monsters may have already been defeated.
    # For example, if B_1 + B_2 < A_1 + A_2, the third hero must defeat at least A_1 + A_2 - (B_1 + B_2) monsters attacking the third town.
    # In such case, the total number of monsters defeated is B_1 + B_2 + ... + B_{N} + (A_1 + A_2 - (B_1 + B_2)) + (A_2 + A_3 - (B_2 + B_3)) + ... + (A_{N} + A_{N+1} - (B_{N} + B_{N+1})).
    # This can be simplified as B_1 + B_2 + ... + B_{N} + A_1 + A_2 + ... + A_{N+1} - (B_1 + B_2 + ... + B_{N} + B_1 + B_2 + ... + B_{N} + B_2 + B_3 + ... + B_{N} + ... + B_{N-1} + B_{N} + B_{N+1})
    # This can be simplified as B_1 + B_2 + ... + B_{N} + A_1 + A_2 + ... + A_{N+1} - (N * B_1 + (N-1) * B_2 + ... + 2 * B_{N-1} + B_N + B_{N+1})

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
