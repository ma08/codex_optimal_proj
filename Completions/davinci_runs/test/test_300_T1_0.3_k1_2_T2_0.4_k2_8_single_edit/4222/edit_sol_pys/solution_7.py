
def main():
    n, k = map(int, input().split())
    a = [0] * n  # 配列を全て0で初期化
    for i in range(k):
        d = int(input())
        b = list(map(int, input().split()))  # 入力をリストに格納
        for j in range(d):
            a[b[j] - 1] += 1
    print(a.count(0))

if __name__ == '__main__':
    main()
