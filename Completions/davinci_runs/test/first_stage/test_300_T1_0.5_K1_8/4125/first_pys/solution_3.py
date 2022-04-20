

def main():
    n, x = map(int, input().split())
    x_i = list(map(int, input().split()))

    # x_iの中で最も大きい値と最も小さい値を求める
    max_x_i = max(x_i)
    min_x_i = min(x_i)

    # 最大値と最小値の差を求める
    diff = max_x_i - min_x_i

    # 最大値と最小値の差を2で割って最大値を求める
    print(diff // 2)

if __name__ == '__main__':
    main()