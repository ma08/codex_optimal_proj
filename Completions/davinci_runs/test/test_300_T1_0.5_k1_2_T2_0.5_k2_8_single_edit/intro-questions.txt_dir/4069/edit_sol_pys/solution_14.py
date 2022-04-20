
import sys
import numpy as np

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < d * k:
        print(abs(x - (x // d) * d)) # 移動回数が少ない時
    else:
        print(abs(x) - (d * k)) # 移動回数が多い時

if __name__ == '__main__':
    main()
