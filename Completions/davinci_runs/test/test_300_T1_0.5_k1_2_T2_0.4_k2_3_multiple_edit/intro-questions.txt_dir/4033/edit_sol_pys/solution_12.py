

def main():
    a, b = map(int, input().split())  # 文字列から数値への変換

    if a == b:  # 同じ数字なら4倍
        print(4 * a)
        return

    if a < b:  # a<bなら入れ替える
        a, b = b, a

    # a >= b
    if (a+b) % 3 == 0:  # 合計が3の倍数ならその半分
        print(2 * (a + b) // 3)
    else:
        print(2 * (a + b) // 3 + 1)


if __name__ == "__main__":
    main()
