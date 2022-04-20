

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def main():
    # 各地点における最大人数を計算
    max_num = [A, B, C, D, E]
    # 移動時間を計算
    time = 0
    # 人数を計算
    num = N
    # 出発地点から出発地点に移動していく
    for i in range(5):
        # 地点における最大人数を超える場合
        if num > max_num[i]:
            # 移動時間を増やす
            time += 1
            # 移動できなかった人数を計算
            num = num - max_num[i]
        # 地点における最大人数以下の場合
        else:
            # 移動時間を増やす
            time += 1
            # 移動できなかった人数を計算
            num = num - num
    # 移動時間を出力
    print(time)

if __name__ == "__main__":
    main()