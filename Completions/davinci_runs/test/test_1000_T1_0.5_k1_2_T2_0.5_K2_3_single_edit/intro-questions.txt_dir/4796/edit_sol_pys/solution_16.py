

def main():
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())
    max_cocktail = min(A//I, B//J, C//K)
    A -= max_cocktail * I
    B -= max_cocktail * J
    C -= max_cocktail * K
    print(A, B, C)


main()
