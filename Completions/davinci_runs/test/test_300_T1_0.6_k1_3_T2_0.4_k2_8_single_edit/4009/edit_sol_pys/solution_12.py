

import sys

def main():
    n, x, y = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    if num[:x+1] == [1] + [0]*x:
        print 0
        return
    if num[:x+1] == [1] + [1]*x:
        print 1
        return
    if num[:y+1] == [1] + [0]*y:
        print 1
        return
    if num[:y+1] == [1] + [1]*y:
        print 0
        return
    for i in range(y+1,x+1):
        if num[i] == 0:
            print 2
            return
    print 1

if __name__ == '__main__':
    main()
