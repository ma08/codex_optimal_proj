

import sys

def main():
    line = sys.stdin.readline().rstrip() # 改行を除いた文字列の入力
    a, b = map(int, line.split()) # 整数の入力
    print(lcm(a, b)) # 最大公約数を出力

def gcd(a, b):
    while b != 0: # bが0になるまで繰り返す
        a, b = b, a % b # 商をbに、剰余をaに代入
    return a

def lcm(a, b):
    return a * b // gcd(a, b) # 最小公倍数を出力

if __name__ == '__main__':
    main()
