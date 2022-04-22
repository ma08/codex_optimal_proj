# https://atcoder.jp/contests/abc148/tasks/abc148_c

import math

def main():
    A, B = map(int, input().split())
    print(A * B // math.gcd(A, B))

if __name__ == '__main__':
    main()
