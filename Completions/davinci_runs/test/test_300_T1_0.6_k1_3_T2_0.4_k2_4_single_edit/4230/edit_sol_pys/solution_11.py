import math


def main():
    x, n = map(int, input().split()) # x: 入力値 n: 個数
    p = sorted(list(map(int, input().split()))) # p: 入力値の配列

    if x < p[0]:
        print(p[0] - x) # 入力値が最小値より小さい場合
    elif x > p[-1]:
        print(x - p[-1]) # 入力値が最大値より大きい場合
    else:
        for i in range(n-1):
            if x < p[i+1]:
                print(min(x-p[i], p[i+1] - x)) # 入力値が最小値より大きく最大値より小さい場合
                break

if __name__ == '__main__':
    main()
