
import sys

def main():
    n, m = map(int, input().split())
    x_s = list(map(int, input().split()))

    x_s.sort()
    min_x = x_s[0]
    max_x = x_s[-1]

    # 数列における各数値の位置を記録する
    # 例えば、数列が[1, 2, 3, 5, 7, 8, 8, 10]であれば、以下の通り
    # position_dict[1] = 0
    # position_dict[2] = 1
    # position_dict[3] = 2
    # position_dict[5] = 3
    # position_dict[7] = 4
    # position_dict[8] = 5
    # position_dict[10] = 7
    position_dict = dict()
    for i, x in enumerate(x_s):
        position_dict[x] = i

    # 数列における各数値の出現回数を記録する
    # 例えば、数列が[1, 2, 3, 5, 7, 8, 8, 10]であれば、以下の通り
    # count_list[0] = 1
    # count_list[1] = 1
    # count_list[2] = 1
    # count_list[3] = 1
    # count_list[4] = 1
    # count_list[5] = 2
    # count_list[7] = 1
    count_list = [0] * len(x_s)
    count_list[0] = 1
    for i in range(1, len(x_s)):
        if x_s[i] == x_s[i - 1]:
            count_list[i] = count_list[i - 1] + 1
        else:
            count_list[i] = 1

    # 各数値における移動回数を記録する
    # 例えば、数列が[1, 2, 3, 5, 7, 8, 8, 10]であれば、以下の通り
    # move_list[0] = 1
    # move_list[1] = 0
    # move_list[2] = 0
    # move_list[3] = 0
    # move_list[4] = 0
    # move_list[5] = 1
    # move_list[7] = 0
    move_list = [0] * len(x_s)
    move_list[0] = 1
    for i in range(1, len(x_s)):
        if x_s[i] == x_s[i - 1]:
            move_list[i] = move_list[i - 1]
        else:
            move_list[i] = move_list[i - 1] + 1

    # 移動回数を計算
    move_count = 0
    for i in range(n):
        # 数列における各数値の位置を計算
        pos = position_dict[min_x + i]

        # 各数値における移動回数を計算
        move_count += move_list[pos]

        # 各数値における移動回数を更新
        if count_list[pos] == 1:
            move_list[pos] = 0
        else:
            move_list[pos] = move_list[pos] - 1

    print(move_count)


if __name__ == "__main__":
    main()
