

import sys

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))

    # 入力された値をソートしておく
    p.sort()

    # リストの左端と右端の値の差を求める
    left = p[0] - X
    right = p[-1] - X

    # 左端と右端の差の絶対値を比べて、大きい方を計算する
    if abs(left) > abs(right):
        if X - left > 0:
            # 左端とXの差が正の数ならば、Xより小さい値が答え
            print(X - left)
        else:
            # 左端とXの差が負の数ならば、Xと左端の差の絶対値が答え
            print(abs(left))
    else:
        if X + right > 0:
            # 右端とXの差が正の数ならば、Xと右端の差の絶対値が答え
            print(abs(right))
        else:
            # 右端とXの差が負の数ならば、Xより小さい値が答え
            print(X + right)

if __name__ == '__main__':
    main()