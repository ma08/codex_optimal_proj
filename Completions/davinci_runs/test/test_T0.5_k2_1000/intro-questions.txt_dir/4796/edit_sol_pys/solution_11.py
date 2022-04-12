

def main():
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())
    max_cocktails = min(A // I, B // J, C // K)
    A -= max_cocktails * I
    B -= max_cocktails * J
    C -= max_cocktails * K
    print(A, B, C)


main()
