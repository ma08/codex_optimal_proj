

def main():
    n, m = map(int, input().split()) # n: 入力数, m: 判定値
    p = list(map(int, input().split())) # p: 入力
    count = 0 # count: 判定値を含む組み合わせ数
    for i in range(n): # i: 先頭値
        for j in range(i, n): # j: 末尾値
            if p[i:j+1].count(m) > 0: # 判定値が含まれている場合
                count += 1 # 判定値を含む組み合わせ数を1増やす
    print(count) # 判定値を含む組み合わせ数を出力

if __name__ == "__main__":
    main()
