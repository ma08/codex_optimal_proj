


def main():
    n,l = map(int, input().split()) # n個の味とl番目の味を取得
    flavor_list = [l + i for i in range(n)] # l番目の味からn個の味を作る
    print(sum(flavor_list[1:])) # 1番目の味からn-1個の味を出力

if __name__ == "__main__":
    main()
