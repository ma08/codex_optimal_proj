

def main():
    n = int(input()) # 人数
    a = int(input()) # アヒル
    b = int(input()) # ハムスター
    c = int(input()) # ハムスター
    d = int(input()) # アヒル
    e = int(input()) # ハムスター

    l = [a, b, c, d, e] # リストに代入
    l.sort() # リストを昇順にソート

    if n <= l[0]: # 人数が最小の部屋数以下なら
        print(1) # 1部屋で収まる
    else:
        print(2) # 2部屋で収まる

if __name__ == '__main__':
    main()
