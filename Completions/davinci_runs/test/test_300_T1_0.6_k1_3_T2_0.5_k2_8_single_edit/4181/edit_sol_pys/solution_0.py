

import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # The first hero can defeat at most B1 monsters attacking the first town, so he will defeat B1 monsters attacking the first town.
    # The second hero can defeat at most B1 + B2 monsters attacking the first and second town, so he will defeat B2 monsters attacking the second town.
    # The i-th hero can defeat at most B1 + B2 + ... + Bi-1 + Bi monsters attacking the first, second, ..., (i-1)-th, and i-th towns, so he will defeat Bi-1 monsters attacking the (i-1)-th town.
    # The last hero can defeat at most B1 + B2 + ... + BN-1 + BN monsters attacking the first, second, ..., (N-1)-th, and N-th towns, so he will defeat BN-1 monsters attacking the (N-1)-th town.
    # The total number of monsters defeated is B1 + B2 + ... + BN-1.
    # However, some monsters may have already been defeated.
    # For example, if B1 + B2 < A1 + A2, the third hero must defeat at least A1 + A2 - (B1 + B2) monsters attacking the third town.
    # In such case, the total number of monsters defeated is B1 + B2 + ... + BN-1 + (A1 + A2 - (B1 + B2)) + (A2 + A3 - (B2 + B3)) + ... + (AN + AN+1 - (BN-1 + BN)).
    # This can be simplified as B1 + B2 + ... + BN-1 + A1 + A2 + ... + AN+1 - (B1 + B2 + ... + BN-1 + B1 + B2 + ... + BN-1 + B2 + B3 + ... + BN-1 + ... + BN-2 + BN-1 + BN)
    # This can be simplified as B1 + B2 + ... + BN-1 + A1 + A2 + ... + AN+1 - (N * B1 + (N-1) * B2 + ... + 2 * BN-1 + BN)

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
