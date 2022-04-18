

def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))

    x_A = [0] * N  # 東京
    x_B = [K] * N  # 大阪
    x_total = x_A + x_B  # 合計
    x_total.sort()

    x_sort = sorted(x)  # 昇順
    x_sort.append(K)

    d = 0  # 全ての距離の合計
    for i in range(N):
        d += abs(x_sort[i] - x_total[i])

    print(d)


if __name__ == "__main__":
    main()
