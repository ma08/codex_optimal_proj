import sys

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))  # 入力されたx_list
    y_list = list(map(int, input().split()))  # 入力されたy_list

    for z in range(x + 1, y):  # x+1からy-1までをzとする
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print("No War")  # zが条件を満たしたら"No War"を出力して終了
            sys.exit()

    print("War")  # zが条件を満たさなかったら"War"を出力して終了

if __name__ == '__main__':
    main()
