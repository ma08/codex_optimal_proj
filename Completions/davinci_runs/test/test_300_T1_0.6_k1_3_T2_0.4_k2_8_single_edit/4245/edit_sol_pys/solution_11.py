

def main():
    a, b = map(int, input().split())  # input()をスペース区切りで数値に変換したものをa, bに代入
    count = 0
    while b > 0:  # bが0より大きい間繰り返す
        if b >= a:  # bがa以上なら
            b -= a
        else:  # bがa未満なら
            b -= 1
        count += 1  # countを1増やす
    print(count)  # countを出力

if __name__ == '__main__':
    main()
