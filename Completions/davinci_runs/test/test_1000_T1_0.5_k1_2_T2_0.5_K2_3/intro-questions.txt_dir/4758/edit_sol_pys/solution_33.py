

    # N, T, M = map(int, input().split()) # map(int, input().split())はリストに変換
    # print(N * T * M, end='')
    # print(N * T * M) # 行末に改行が入る
def main():
    N, T, M = map(int, input().split())
    print(N * T * M, end='') # end=''は行末に改行が入らない

if __name__ == "__main__":
    main()
