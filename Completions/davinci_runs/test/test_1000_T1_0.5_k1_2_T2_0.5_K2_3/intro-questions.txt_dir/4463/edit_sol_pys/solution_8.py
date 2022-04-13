def main():
    # 1行目
    n = int(input())
    # 2行目
    a = list(map(int, input().split()))
    # 3行目
    b = list(map(int, input().split()))


    # 標準入力閉じる
    # 入力を受け取った後に処理を行うため
    # input_file.close()

    # 出力
    # print(n)
    # print(a)
    # print(b)
    # print(a + b)

    # リストの中身を出力
    # print(' '.join(map(str, a)))
    # print(' '.join(map(str, b)))
    print(' '.join(map(str, a + b)))

if __name__ == '__main__':
    main()
