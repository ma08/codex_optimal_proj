

import sys

def main():
    h, w, n = [int(x) for x in raw_input().strip().split()]
    bricks = [int(x) for x in raw_input().strip().split()]
    if sum(bricks) >= h * w:
        print 'yes'
    else:
        print 'no'

if __name__ == '__main__':
    main()
