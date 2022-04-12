
import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < k * d:
        print(abs(x - (x // d) * d)) # x - (x // d) * d は x の d の倍数に最も近い値
    else:
        print(abs(x) - (k * d))

if __name__ == '__main__':
    main()
