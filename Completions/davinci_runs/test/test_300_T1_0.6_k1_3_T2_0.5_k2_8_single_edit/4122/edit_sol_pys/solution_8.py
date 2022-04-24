

import sys

def solve():
    h, n = map(int, input().split()) # h:体力、n:魔法の数
    d = list(map(int, input().split())) # d:魔法の効果
    for i in range(n):
        h += d[i] # 体力を増やす
        if h <= 0:
            return i + 1 # 倒れたら回数を返す
    return -1 # 倒れなかったら-1を返す

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    print(solve())
