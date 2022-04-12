

def main():
    a, b, c = map(int, input().split())
    i, j, k = map(int, input().split())
    max_cocktail = min(a // i, b // j, c // k)
    a -= max_cocktail * i
    b -= max_cocktail * j
    c -= max_cocktail * k
    print(a, b, c)


main()
