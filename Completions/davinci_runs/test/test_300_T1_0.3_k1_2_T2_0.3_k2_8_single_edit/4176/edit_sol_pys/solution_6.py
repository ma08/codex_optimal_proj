
import sys

def main():
    line = sys.stdin.readline().rstrip()  # 改行を除いた文字列を取得
    a, b = map(int, line.split())  # 整数に変換
    print(lcm(a, b))  # 最小公倍数を出力

def gcd(a, b):
    while b != 0:  # bが0になるまで
        a, b = b, a % b  # bをaとbの差で更新
    return a  # bが0になった時点でのaが最大公約数

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    main()
