

def main():
    x, y = map(int, input().split())  # input は str 型なので int 型に変換
    if x <= 4 and y <= 4:
        print('Yes')
    elif x <= 8 and y <= 8:  # <= は < 以下
        print('Yes')
    elif x <= 12 and y <= 12:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':  # これは関数の中に入れる
    main()
