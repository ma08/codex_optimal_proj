
def main():
    N, T, M = map(int, input().split()) # N: 数字の桁数, T: 各桁の数字を決めるのにかかる時間, M: 各桁の数字を決めるのに使う回数
    print(N * T * M)

if __name__ == "__main__":
    main()
