
import math

def main():
    A, B = map(int, input().split()) # A, B をそれぞれint型で取得
    print(A * B // math.gcd(A, B)) # A, B の最大公約数で割った結果を出力

if __name__ == '__main__':
    main()
