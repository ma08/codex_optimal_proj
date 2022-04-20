

def main():
    a, b = map(int, input().split())  # inputをsplitで分割して、それをmapでintに変換してa, bに代入

    if a == b:  # aとbが一緒なら
        print(4 * a)  # 4倍して出力
    else:  # それ以外なら
        print(2 * (a + b))  # 2倍して出力

if __name__ == "__main__":
    main()
