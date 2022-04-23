

import numpy as np

def main():
    # Read Inputs
    N = int(input())
    A = list(map(int, input().split()))

    # Init
    ans = 0

    # Calcs
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
            ans += 1

    # Print Answer
    print(ans, flush=True)

if __name__ == '__main__':
    main()
