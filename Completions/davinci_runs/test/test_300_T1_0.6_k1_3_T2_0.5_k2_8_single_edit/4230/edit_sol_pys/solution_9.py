
import sys

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))

    # 入力された値をソート
    p.sort()

    # リストの左端と右端の値の差を求め
    left = p[0] - X
    right = p[-1] - X

    # 左端と右端の差の絶対値を比べ、大きい方を計算
    if abs(left) > abs(right):
        if X - left > 0:
            # 左端とXの差が正の数なら、Xより小さい値が答え
            print(X - left)
        else:
            # 左端とXの差が負の数なら、Xと左端の差の絶対値が答え
            print(abs(left))
    else:
        if X + right > 0:
            # 右端とXの差が正の数なら、Xと右端の差の絶対値が答え
            print(abs(right))
        else:
            # 右端とXの差が負の数なら、Xより小さい値が答え
            print(X + right)

if __name__ == '__main__':
    main()
