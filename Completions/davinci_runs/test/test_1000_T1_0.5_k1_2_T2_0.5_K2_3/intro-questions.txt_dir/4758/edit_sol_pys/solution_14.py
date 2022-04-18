
def main():
    N, T, M = map(int, input().split())  # N: パンの量, T: 1人当たりのパンの最大消費量, M: 村の人数,
    print(N * T * M)  # 全体で必要なパンの量,


if __name__ == "__main__":
    main()
