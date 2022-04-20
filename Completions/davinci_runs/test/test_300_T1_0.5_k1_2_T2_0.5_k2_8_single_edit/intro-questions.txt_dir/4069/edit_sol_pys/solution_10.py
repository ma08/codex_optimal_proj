

import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < k * d:
        print(abs(x - (x // d) * d)) # 小さいならそのまま
    else:
        print(abs(x) - (k * d)) # 大きいなら、移動回数を減らしていく

if __name__ == '__main__':
    main()
