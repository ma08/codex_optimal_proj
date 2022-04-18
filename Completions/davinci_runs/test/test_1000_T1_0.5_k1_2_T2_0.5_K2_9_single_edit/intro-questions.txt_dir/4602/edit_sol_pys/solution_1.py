

def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))

    x_A = [0] * N  # リストの初期化
    x_B = [K] * N  # リストの初期化
    x_total = x_A + x_B  # リストの結合
    x_total.sort()  # リストのソート

    x_sort = sorted(x)  # リストのソート
    x_sort.append(K)  # リストの追加

    d = 0
    for i in range(N):
        d += abs(x_sort[i] - x_total[i])

    print(d)


if __name__ == "__main__":
    main()
