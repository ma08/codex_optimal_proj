
import sys

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))  # 入力された値をソートしておく

    if n == 0:
        print(x)
        sys.exit()

    p.sort()  # リストの左端と右端の値の差を求める
    left = p[0] - x
    right = p[-1] - x

    if abs(left) > abs(right):
        if x - left > 0:
            print(x - left)  # 左端とXの差が正の数ならば、Xより小さい値が答え
        else:
            print(abs(left))  # 左端とXの差が負の数ならば、Xと左端の差の絶対値が答え
    else:
        if x + right > 0:
            print(abs(right))  # 右端とXの差が正の数ならば、Xと右端の差の絶対値が答え
        else:
            print(x + right)  # 右端とXの差が負の数ならば、Xより小さい値が答え


if __name__ == '__main__':
    main()
