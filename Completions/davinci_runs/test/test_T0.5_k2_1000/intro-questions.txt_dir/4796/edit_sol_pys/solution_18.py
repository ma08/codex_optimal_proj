
def main():
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())

    min_cocktail = min(A / I, B / J, C / K)  # 最小のカクテルの個数

    print(max(A - I * min_cocktail, 0))  # コップに入っている水の量
    print(max(B - J * min_cocktail, 0))  # コップに入っている水の量
    print(max(C - K * min_cocktail, 0))  # コップに入っている水の量


if __name__ == "__main__":
    main()
