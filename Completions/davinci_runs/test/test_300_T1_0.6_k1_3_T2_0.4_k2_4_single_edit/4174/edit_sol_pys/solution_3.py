

def main():
    n, x = map(int, input().split()) # n : 個数, x : 合計値
    l = list(map(int, input().split())) # l : 個数分のリスト
    s = 0
    cnt = 0
    for i in range(n):
        s += l[i] # s : 合計値
        if s <= x: # 合計値がx以下ならカウント
            cnt += 1
    print(cnt) # 出力

if __name__ == '__main__':
    main()
