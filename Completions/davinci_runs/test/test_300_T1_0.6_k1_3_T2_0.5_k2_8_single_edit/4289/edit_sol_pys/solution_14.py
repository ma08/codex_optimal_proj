
def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    temp = [abs(t - h[i] * 0.006 - a) for i in range(n)]  # リスト内包表記
    print(temp.index(min(temp)) + 1)  # min()で最小値を取得し、そのインデックスを+1して出力


if __name__ == "__main__":
    main()
