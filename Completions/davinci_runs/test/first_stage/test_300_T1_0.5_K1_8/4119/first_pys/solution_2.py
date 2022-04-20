


def main():
    n, m = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.sort()

    # 左端と右端の距離を計算
    x_left = x_list[0]
    x_right = x_list[-1]
    x_distance = x_right - x_left

    # 左端から右端までの距離を計算
    x_sum = sum(x_list)
    x_sum_distance = x_sum - x_left - x_right

    # 左端と右端の距離が短い方を移動させる
    if x_distance < x_sum_distance:
        print(x_sum_distance)
    else:
        print(x_distance)


if __name__ == '__main__':
    main()