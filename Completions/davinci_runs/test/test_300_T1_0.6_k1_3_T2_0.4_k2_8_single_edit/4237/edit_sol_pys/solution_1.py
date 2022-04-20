
from math import gcd

def main():
    A,B,C,D = map(int,input().split())
    lcm = C*D // gcd(C,D)
    print(B//lcm - (A-1)//lcm)

if __name__ == '__main__':
    main()
