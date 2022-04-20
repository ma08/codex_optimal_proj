

import sys
import math

def main():
    n, x, y = [int(i) for i in raw_input().split()]
    num = raw_input()
    num = num[::-1]
    total = 0
    for i in range(n):
        if i < x:
            if i < y:
                if num[i] == '0':
                    total += 1
            else:
                if num[i] == '1':
                    total += 1
        else:
            if num[i] == '1':
                total += 1
    print total
            
if __name__ == '__main__':
    main()