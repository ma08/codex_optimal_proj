
import sys

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split())) # 入力を1行にまとめて、空白で区切り、int型にキャストしてリスト化
    y_list = list(map(int, input().split())) # 入力を1行にまとめて、空白で区切り、int型にキャストしてリスト化

    for z in range(x + 1, y):
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print("No War")
            sys.exit()

    print("War")

if __name__ == '__main__':
    main()
