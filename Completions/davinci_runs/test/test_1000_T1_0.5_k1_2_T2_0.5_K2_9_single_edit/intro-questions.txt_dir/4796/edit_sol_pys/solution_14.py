

def main():
    a, b, c = map(int, input().split())
    i, j, k = map(int, input().split())

    min_cocktail = min(a / i, b / j, c / k)

    print(max(a - i * min_cocktail, 0))
    print(max(b - j * min_cocktail, 0))
    print(max(c - k * min_cocktail, 0))


if __name__ == "__main__":
    main()
