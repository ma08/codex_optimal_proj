

import sys

def gcd(a,b):
    if a < b:
        a,b = b,a
    while a % b != 0:
        a,b = b,a%b
    return b

def gcd3(a,b,c):
    return gcd(a,gcd(b,c))

def main():
    for line in sys.stdin:
        K = int(line)
        print(sum(gcd3(a,b,c) for a in range(1,K+1) for b in range(1,K+1) for c in range(1,K+1)))

if __name__ == '__main__':
    main()