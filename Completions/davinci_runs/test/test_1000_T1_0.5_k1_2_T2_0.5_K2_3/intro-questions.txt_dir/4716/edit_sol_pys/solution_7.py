

def main():
    N, K = map(int, input().split())  # N: 個数, K: 上位何位までを足すか
    L = sorted(map(int, input().split()), reverse=True)  # リスト
    print(sum(L[:K]))  # 上位K位までを足す

if __name__ == '__main__':
    main()
