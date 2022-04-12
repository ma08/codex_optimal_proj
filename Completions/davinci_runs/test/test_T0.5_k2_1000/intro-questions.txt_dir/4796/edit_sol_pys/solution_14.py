
def main():
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())

    min_cocktail = min(A / I, B / J, C / K)  # 最大で何個作れるか

    print(max(A - I * min_cocktail, 0))  # 最大で何個作れるかを引いた残り
    print(max(B - J * min_cocktail, 0))  # 最大で何個作れるかを引いた残り
    print(max(C - K * min_cocktail, 0))  # 最大で何個作れるかを引いた残り


if __name__ == "__main__":
    main()
