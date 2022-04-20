

def main():
    k, x = map(int, input().split()) # 入力
    for i in range(x - k + 1, x + k): # 範囲を計算
        print(i, end=" ") # 出力

if __name__ == '__main__':
    main()
