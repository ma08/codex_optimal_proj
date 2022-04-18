
import sys

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))[:n]

    # 入力された値をソートしておく
    p.sort()

    # リストの左端と右端の値の差を求める
    left = p[0] - x
    right = p[-1] - x

    # 左端と右端の差の絶対値を比べて、大きい方を計算する
    if abs(left) > abs(right):
        if x - left > 0:
            # 左端とxの差が正の数ならば、xより小さい値が答え
            print(x - left)
        else:
            # 左端とxの差が負の数ならば、xと左端の差の絶対値が答え
            print(abs(left))
    else:
        if x + right > 0:
            # 右端とxの差が正の数ならば、xと右端の差の絶対値が答え
            print(abs(right))
        else:
            # 右端とxの差が負の数ならば、xより小さい値が答え
            print(x + right)

if __name__ == '__main__':
    main()
