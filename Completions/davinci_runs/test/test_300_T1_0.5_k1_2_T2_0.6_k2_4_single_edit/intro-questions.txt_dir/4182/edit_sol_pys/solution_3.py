import sys

def main():
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))  # 入力受け取り
    y_list = list(map(int, input().split()))  # 入力受け取り

    for x in range(X + 1, Y):
        if all(x > x_i for x_i in x_list) and all(x <= y_i for y_i in y_list):
            print("No War")  # 出力
            sys.exit()  # 処理終了

    print("War")  # 出力

if __name__ == '__main__':
    main()
