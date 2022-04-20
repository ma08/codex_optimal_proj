
import sys

def main():
    n, m, x, y = map(int, input().split())  # n: 都市の数, m: 道路の数, x: 国境の西側, y: 国境の東側
    x_list = list(map(int, input().split()))  # 道路の西端の座標
    y_list = list(map(int, input().split()))  # 道路の東端の座標

    for z in range(x + 1, y):
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):  # 条件を満たすかどうか
            print("No War")
            sys.exit()

    print("War")

if __name__ == '__main__':
    main()
