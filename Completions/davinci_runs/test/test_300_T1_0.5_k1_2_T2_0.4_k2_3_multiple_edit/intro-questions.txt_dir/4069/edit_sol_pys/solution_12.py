
import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) <= k * d:
        print(abs(x - (x // d) * d))  # 小さい方の距離
    else:
        print(abs(x) - (k * d))  # 大きい方の距離

if __name__ == '__main__':
    main()
