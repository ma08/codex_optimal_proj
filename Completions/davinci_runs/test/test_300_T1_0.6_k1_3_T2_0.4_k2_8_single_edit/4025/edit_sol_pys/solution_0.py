

def main():
    a, b, c = [int(x) for x in input().split()]  # 入力を分割して整数に変換

    if a + b + c > 7:  # 合計が7より大きければ7
        print(7)  # 7を出力
    else:
        print(a + b + c)  # そうでなければ合計を出力


if __name__ == '__main__':
    main()
