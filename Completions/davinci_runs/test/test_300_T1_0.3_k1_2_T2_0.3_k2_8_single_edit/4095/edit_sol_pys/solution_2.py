

def main():
    n, m = map(int, input().split()) # n:配列の要素数, m:探す値
    p = list(map(int, input().split())) # 配列
    count = 0
    for i in range(n): # 配列の要素数分ループ
        for j in range(i, n): # 配列の要素数分ループ
            if p[i:j+1].count(m) > 0: # 配列の要素数分ループ
                count += 1
    print(count)

if __name__ == "__main__":
    main()
