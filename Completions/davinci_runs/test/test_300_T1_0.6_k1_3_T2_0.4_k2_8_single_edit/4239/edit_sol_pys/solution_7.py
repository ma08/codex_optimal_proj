
import sys
import io
import math


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    n = int(input())  # 整数の入力
    count = 0
    while n > 0:  # 入力値が0になるまでループ
        if n % 6 == 0:
            n -= 6  # 6で割り切れる場合は6を引く
            count += 1  # 割り切れた回数をカウント
        elif n % 9 == 0:
            n -= 9  # 9で割り切れる場合は9を引く
            count += 1  # 割り切れた回数をカウント
        else:
            n -= 1  # 6でも9でも割り切れない場合は1を引く
            count += 1  # 割り切れなかった回数をカウント
    print(count)


if __name__ == '__main__':
    main()
