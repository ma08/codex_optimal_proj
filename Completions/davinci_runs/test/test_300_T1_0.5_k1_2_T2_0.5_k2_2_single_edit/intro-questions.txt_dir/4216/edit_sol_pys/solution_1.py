# -*- coding: utf-8 -*-
import math

def main():
    N = int(input())
    r = math.ceil(math.sqrt(N))
    for i in range(r, 0, -1):  # rから1まで-1ずつ
        if N % i == 0:
            print(N // i // 10 ** (len(str(i)) - 1))  # 上位桁を取得
            break

if __name__ == '__main__':
    main()
