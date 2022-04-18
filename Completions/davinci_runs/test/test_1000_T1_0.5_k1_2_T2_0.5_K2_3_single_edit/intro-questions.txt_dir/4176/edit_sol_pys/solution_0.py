
import sys

def main():
    # input
    A, B = map(int, sys.stdin.readline().split())
    # output
    print(lcm(A, B))

def lcm(A, B):
    """
    最小公倍数を求める
    """
    return A * B // gcd(A, B)

def gcd(A, B):
    """
    最大公約数を求める
    """
    while B:
        A, B = B, A % B
    return A

if __name__ == '__main__':
    main()
