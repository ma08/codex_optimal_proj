

import sys

def main():
    a,b = map(int,input().split()) # a,b = map(int,sys.stdin.readline().split())
    print((a+b)%24)

if __name__ == '__main__':
    main()
