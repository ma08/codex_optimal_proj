

from math import gcd

def main():
    A,B,C,D = map(int,input().split())
    # 最小公倍数
    lcm = C*D // gcd(C,D)
    # A~Bまでのlcmの倍数を引く
    print(B//lcm - (A-1)//lcm)

if __name__ == '__main__':
    main()