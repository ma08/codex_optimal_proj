

import math

def main():
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())

    min_cocktail = min(A / I, B / J, C / K)

    print(math.floor(max(A - I * min_cocktail, 0)))
    print(math.floor(max(B - J * min_cocktail, 0)))
    print(math.floor(max(C - K * min_cocktail, 0)))


if __name__ == "__main__":
    main()
