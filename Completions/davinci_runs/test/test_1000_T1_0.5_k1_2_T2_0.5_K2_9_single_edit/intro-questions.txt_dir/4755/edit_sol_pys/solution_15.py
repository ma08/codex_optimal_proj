

import sys

def main():
    # Get the inputs
    C, K = [int(x) for x in raw_input().split()]

    # Round to nearest 10^K
    C = C // (10**K) * (10**K)
    if C == 0:
        C += 1
    print(C)

if __name__ == "__main__":
    main()
