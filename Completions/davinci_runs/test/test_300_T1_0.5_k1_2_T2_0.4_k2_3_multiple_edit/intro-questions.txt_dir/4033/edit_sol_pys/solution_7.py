

def main():
    a, b = map(int, input().split())  # aとbをint型に変換してaとbに代入

    if a == b:
        print(4 * a + 1)  # 4a+1を出力
    else:
        print(2 * (a + b) + 1)  # 2(a+b)+1を出力

if __name__ == "__main__":
    main()
