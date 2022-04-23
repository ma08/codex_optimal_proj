

def main():
    n = int(input()) # 料理の数
    a = int(input()) # 1人目の料理作り時間
    b = int(input()) # 2人目の料理作り時間
    c = int(input()) # 3人目の料理作り時間
    d = int(input()) # 4人目の料理作り時間
    e = int(input()) # 5人目の料理作り時間

    l = [a, b, c, d, e] # 作り時間のリスト
    l.sort() # 作り時間を昇順にソート

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
