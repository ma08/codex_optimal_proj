
def main():
    n = int(input())  # 1行目
    heights = list(map(int, input().split()))  # 2行目

    for i in range(1, n):  # 1からn-1まで繰り返す
        if heights[i - 1] > heights[i]:  # i-1番目の要素がi番目の要素より大きい場合
            heights[i] += 1

    for i in range(1, n):  # 1からn-1まで繰り返す
        if heights[i - 1] > heights[i]:  # i-1番目の要素がi番目の要素より大きい場合
            print('No')
            break
    else:  # for文が正常に実行された場合
        print('Yes')


if __name__ == '__main__':
    main()
