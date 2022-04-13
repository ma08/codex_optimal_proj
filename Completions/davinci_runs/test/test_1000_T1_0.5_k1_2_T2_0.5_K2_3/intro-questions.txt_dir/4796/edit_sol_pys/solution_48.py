

def main():
    A, B, C = map(int, input().split())  # 1行目
    I, J, K = map(int, input().split())  # 2行目

    min_cocktail = min(A // I, B // J, C // K)

    print(max(A - I * min_cocktail, 0), max(B - J * min_cocktail, 0), max(C - K * min_cocktail, 0))


if __name__ == "__main__":
    main()
