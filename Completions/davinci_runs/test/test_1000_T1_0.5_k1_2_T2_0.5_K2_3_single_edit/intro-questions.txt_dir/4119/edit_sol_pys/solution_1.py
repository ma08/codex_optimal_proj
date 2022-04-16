
import sys

def main():
    n, m = map(int, input().split())
    x_s = list(map(int, input().split()))

    x_s.sort()
    min_x = x_s[0]
    max_x = x_s[-1]

    # 数列における各数値の位置を記録
    # 例えば、数列が[1, 2, 3, 5, 7, 8, 8, 10]であれば、以下のようになる
    # position_dict = {1: 0, 2: 1, 3: 2, 5: 3, 7: 4, 8: 5, 10: 7}
    position_dict = dict()
    for i, x in enumerate(x_s):
        position_dict[x] = i

        # 例えば、数列が[1, 2, 3, 5, 7, 8, 8, 10]であれば、以下のようになる
        # count_list = [1, 1, 1, 1, 1, 2, 2, 1]
    count_list = [0] * len(x_s)
    count_list[0] = 1
    for i in range(1, len(x_s)):
        if x_s[i] == x_s[i - 1]:
            count_list[i] = count_list[i - 1] + 1
        else:
            count_list[i] = 1

    # 各数値における移動回数を記録
    # 例えば、数列が[1, 2, 3, 5, 7, 8, 8, 10]であれば、以下のようになる
    # move_list = [1, 0, 0, 0, 0, 1, 1, 0]
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
