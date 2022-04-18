

def main():
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())

    min_cocktail = min(A / I, B / J, C / K)  # 最少で作れるカクテル

    print(A - I * min_cocktail, B - J * min_cocktail, C - K * min_cocktail)


if __name__ == "__main__":
    main()
