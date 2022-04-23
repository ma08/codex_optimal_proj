
import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < k * d: # 右に行く場合
        print(abs(x - (x // d) * d)) # 右に行く場合
    else:
        print(abs(x) - (k * d)) # 左に行く場合

if __name__ == '__main__':
    main()
