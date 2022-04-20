
import sys

def main():
    n, m, x, y = map(int, input().split())  # n:高橋くんの足の数, m:青木くんの足の数, x:高橋くんの足の長さ, y:青木くんの足の長さ
    x_list = list(map(int, input().split()))  # 高橋くんの足の長さのリスト
    y_list = list(map(int, input().split()))  # 青木くんの足の長さのリスト

    for z in range(x + 1, y):
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print("No War")
            sys.exit()

    print("War")

if __name__ == '__main__':
    main()
