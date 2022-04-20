# coding: utf-8

import sys

def main():
    line = sys.stdin.readline().rstrip('\r\n')  # 改行コードを削除
    a, b = map(int, line.split())  # 整数に変換

    for i in range(1, 100):  # 1から100まで
        if int(i * 1.08) == a and int(i * 1.1) == b:  # 条件を満たす数字があるか
            print(i)
            sys.exit()
    print(-1)

if __name__ == '__main__':
    main()
