def main():
    # 1行目
    n = int(input())
    # 2行目
    a = list(map(int, input().split()))
    # 3行目
    b = list(map(int, input().split()))
    # リストの中身を出力
    # print(' '.join(map(str, a)))
    # print(' '.join(map(str, b)))
    print(' '.join(map(str, a + b)))


    # 入力を受け取った後に処理を行うために標準入力を閉じる
    input_file.close()


if __name__ == '__main__':
    main()
