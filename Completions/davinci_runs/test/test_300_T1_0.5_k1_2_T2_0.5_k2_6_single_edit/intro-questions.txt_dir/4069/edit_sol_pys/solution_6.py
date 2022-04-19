import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < k * d:
        print(abs(x - (x // d) * d))  # 小さい場合
    else:
        print(abs(x) - (k * d))  # 大きい場合

if __name__ == '__main__':
    main()
