

def main():
    a, b, c = map(int, input().split())
    i, j, k = map(int, input().split())

    min_cocktail = min(a / i, b / j, c / k)  # 最大で何個作れるか

    print(max(a - i * min_cocktail, 0))  # 最大で何個作れるかを引いた残り
    print(max(b - j * min_cocktail, 0))  # 最大で何個作れるかを引いた残り
    print(max(c - k * min_cocktail, 0))  # 最大で何個作れるかを引いた残り


if __name__ == "__main__":
    main()
