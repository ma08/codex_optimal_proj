


def main():
    N, D = map(int, input().split())

    # 観測者の数
    inspector = 0

    # 観測者を配置する位置
    position = 0

    for i in range(N):
        # 観測者がいない場合は観測者を配置する
        if i > position + D:
            inspector += 1
            position = i
        # 観測者がいる場合は観測者が配置した位置を更新する
        else:
            position = max(i, position)

    print(inspector)


if __name__ == '__main__':
    main()