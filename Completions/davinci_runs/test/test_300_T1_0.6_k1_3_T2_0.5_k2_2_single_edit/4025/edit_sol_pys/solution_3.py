

def main():
    a, b, c = [int(x) for x in input().split()]  # inputをスペースで区切ってリストに格納

    if a + b + c > 7:  # 合計が7を超える場合
        print(7)  # 7を返す
    else:
        print(a + b + c)  # 合計を返す


if __name__ == '__main__':  # このファイルが直接実行された場合のみmain()を実行
    main()  # main()関数を呼び出す
