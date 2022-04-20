# coding: utf-8


def main():
    n = int(input())
    p = list(map(int, input().split())) # listに変換する
    count = 0

    for i in range(1, n-1): # 配列の最初と最後を除く
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
