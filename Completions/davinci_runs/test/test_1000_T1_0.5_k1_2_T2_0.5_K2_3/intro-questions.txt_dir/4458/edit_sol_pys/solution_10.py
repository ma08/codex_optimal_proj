

import sys,math

def main():
    n,a,b = map(int,input().split())
    print(math.ceil(n/(a+b))*a)

if __name__ == '__main__':
    main()
