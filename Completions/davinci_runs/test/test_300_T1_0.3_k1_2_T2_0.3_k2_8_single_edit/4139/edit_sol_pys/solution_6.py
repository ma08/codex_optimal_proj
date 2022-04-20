

def main():
    n = int(input())  # 入力
    count = 0  # 出力
    for i in range(1, n+1):  # 1からnまでの数字を繰り返し
        if '7' in str(i) and '5' in str(i) and '3' in str(i):  # 数字の中に7,5,3が含まれているか
            count += 1  # 含まれていたらカウント
    print(count)  # 出力

if __name__ == '__main__':
    main()
