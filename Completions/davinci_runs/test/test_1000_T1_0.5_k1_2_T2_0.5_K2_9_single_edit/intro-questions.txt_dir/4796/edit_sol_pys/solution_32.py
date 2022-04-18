

def main():
    A, B, C = map(float, input().split())
    I, J, K = map(float, input().split())

    min_cocktail = min(A / I, B / J, C / K)

    print(max(A - I * min_cocktail, 0), max(B - J * min_cocktail, 0), max(C - K * min_cocktail, 0), sep=" ")


if __name__ == "__main__":
    main()
