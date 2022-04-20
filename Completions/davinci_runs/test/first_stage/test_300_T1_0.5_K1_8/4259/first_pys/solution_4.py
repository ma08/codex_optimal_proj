

import sys

def main():
    K = int(input())
    A, B = map(int,input().split())
    if A % K == 0 or B % K == 0:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()