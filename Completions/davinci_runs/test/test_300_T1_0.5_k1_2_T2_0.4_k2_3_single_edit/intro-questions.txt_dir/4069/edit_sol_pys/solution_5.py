
import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < k * d:  # 初めて移動できるまでの移動距離がk*dより小さい場合
        print(abs(x - (x // d) * d))  # 初めて移動できるまでの移動距離
    else:
        print(abs(x) - (k * d))  # 初めて移動できるまでの移動距離がk*dより大きい場合

if __name__ == '__main__':
    main()
