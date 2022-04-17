

def main():
    a, b = map(int, input().split())  # a,bをint型に変換しておく
    if a == 1 or b == 1:
        print(a*b)  # どちらかが1ならば、それぞれを掛け合わせる
    elif a == 2:
        if b == 2 or b == 3 or b == 5 or b == 7:  # bが2,3,5,7ならば、掛け合わせる
            print(a*b)  # 掛け合わせる
        else:
            print(-1)  # それ以外ならば、-1を出力
    elif a == 3:
        if b == 2 or b == 3 or b == 5 or b == 7:  # bが2,3,5,7ならば、掛け合わせる
            print(a*b)  # 掛け合わせる
        else:
            print(-1)  # それ以外ならば、-1を出力
    elif a == 4:
        if b == 3 or b == 5 or b == 7:  # bが3,5,7ならば、掛け合わせる
            print(a*b)  # 掛け合わせる
        else:
            print(-1)  # それ以外ならば、-1を出力
    elif a == 5:
        if b == 2 or b == 3 or b == 5 or b == 7:  # bが2,3,5,7ならば、掛け合わせる
            print(a*b)  # 掛け合わせる
        else:
            print(-1)  # それ以外ならば、-1を出力
    elif a == 6:
        if b == 5 or b == 7:  # bが5,7ならば、掛け合わせる
            print(a*b)  # 掛け合わせる
        else:
            print(-1)  # それ以外ならば、-1を出力
    elif a == 7:
        if b == 2 or b == 3 or b == 5 or b == 7:  # bが2,3,5,7ならば、掛け合わせる
            print(a*b)  # 掛け合わせる
        else:
            print(-1)  # それ以外ならば、-1を出力
    elif a == 8:
        if b == 3 or b == 5 or b == 7:  # bが3,5,7ならば、掛け合わせる
            print(a*b)  # 掛け合わせる
        else:
            print(-1)  # それ以外ならば、-1を出力
    elif a == 9:
        if b == 2 or b == 3 or b == 5 or b == 7:  # bが2,3,5,7ならば、掛け合わせる
            print(a*b)  # 掛け合わせる
        else:
            print(-1)  # それ以外ならば、-1を出力
    else:
        print(-1)  # それ以外ならば、-1を出力

if __name__ == '__main__':
    main()
